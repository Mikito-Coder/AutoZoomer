import Quickstart
import datetime
import webbrowser
import time


# Call the main function and store its return value in 'bank'
bank = Quickstart.main()

print(bank)
# print(Quickstart.bank)



# Your meetings dictionary


def schedule_meetings(meetings):
    # Get current date and time
    now = datetime.datetime.now()

    for meeting_name, (link, time_str) in meetings.items():
        # Parse the meeting time
        meeting_time = datetime.datetime.strptime(time_str, "%H:%M").replace(year=now.year, month=now.month, day=now.day)
        
        # Calculate wait time in seconds
        wait_time_sec = (meeting_time - now).total_seconds()

        # Schedule the meeting if it's later today
        if wait_time_sec > 0:
            print(f"Scheduled {meeting_name} in {wait_time_sec / 60:.2f} minutes.")
            time.sleep(wait_time_sec)
            webbrowser.open(link)
        else:
            print(f"{meeting_name} time has passed for today.")

schedule_meetings(bank)