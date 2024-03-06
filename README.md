# AutoZoomer

## Overview

AutoZoomer is a Python-based automation tool designed to streamline the process of joining Zoom meetings directly from your Google Calendar events. This tool interacts with the Google Calendar API to fetch upcoming events, identifies those that include Zoom meeting links, and automatically launches them in your browser at the appropriate times.

## Features

- **Google Calendar Integration**: Seamlessly fetches your upcoming calendar events to identify those with Zoom meeting links.
- **Automatic Meeting Identification**: Filters through events to find and extract Zoom meeting links located in the location field.
- **Intelligent Scheduling**: Calculates the start time of each meeting and launches the Zoom link just before the meeting begins.
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux systems, requiring only Python and internet access.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Access to Google Calendar API
- `google-auth`, `google-auth-oauthlib`, and `google-auth-httplib2` Python packages

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Mikito-Coder/autozoomer.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd autozoomer
   ```
3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Follow the [Google Calendar API Quickstart](https://developers.google.com/calendar/quickstart/python) to set up access to your Google Calendar.
2. **Run the script**:
   ```bash
   python autozoomer.py
   ```

## How It Works

AutoZoomer utilizes the Google Calendar API to access your upcoming events. It identifies events with Zoom links by scanning the `location` field for recognizable Zoom URL patterns. When it finds an event with a Zoom link, the script schedules the opening of this link in your default web browser, ensuring you join your meetings on time without manual intervention.

## Contributing

Contributions to AutoZoomer are welcome! Whether it's feature suggestions, bug reports, or code contributions, please feel free to make a pull request or open an issue.


