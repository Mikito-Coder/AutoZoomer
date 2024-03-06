import datetime
import os.path

import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def main():
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    print("Getting the upcoming 10 events")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])
   
    #Keeps the zoom link information, Event name and the time
    bank={}
    if not events:
      print("No upcoming events found.")
      return
    else:

       
        for event in events:
            start_str = event["start"].get("dateTime", event["start"].get("date"))
            if "T" in start_str:
                start_formatted = start_str[11:16].replace("T", " ")
            else:
                start_formatted = start_str

            # Directly access the 'location' field.
            location = event.get("location", "")


            # If the 'location' field contains the Zoom link directly, print it; no need for further checks.
            if "zoom.us" in location:
                bank[event['summary']] = (location,start_formatted)  
                # print(f"Event: {event['summary']}, Start Time: {start_formatted}, Zoom Link: {location}")
        print(bank)
            # else:
            #     print(f"Event: {event['summary']}, Start Time: {start_formatted} - No Zoom link found")
    return bank








    #   print(json.dumps(events, indent = 4))
    #   for event in events:
    #     loc = event.get('location','no loaction')
    #     des= event.get('summary')
    #     print(des,loc)
      



        # for event in events:
        #     start_str = event["start"].get("dateTime", event["start"].get("date"))
    
        #     # Check if we have a dateTime value
        #     if "T" in start_str:
        #         # Simplified approach: Remove the seconds and timezone part, assuming format consistency
        #         # Example: "2024-02-19T15:00:00-05:00" -> "2024-02-19 15:00"
        #         start_formatted = start_str[:16].replace("T", " ")
        #     else:
        #         # For all-day events, just use the date
        #         start_formatted = start_str

        #     print(f"Event: {event['summary']}, Start Time: {start_formatted}")

            
    # print(f"Event: {event['summary']}, Start Time: {start_formatted}")

    #Normal time annd date not formatted 
    #   for event in events:
    # # Print summary and start time of each event
    #     print(f"Event: {event['summary']}, Start Time: {event['start']['dateTime']}")

    #   print(json.dumps(events, indent = 4))

    # Prints the start and name of the next 10 events
        # for event in events:
        #     start = event["start"].get("dateTime", event["start"].get("date"))
        #     print(start, event["summary"])

  except HttpError as error:
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()