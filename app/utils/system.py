import os
import webbrowser
import datetime
import re

def open_app(app_name: str):
    apps = {
        "instagram": "https://www.instagram.com/",
        "youtube": "https://www.youtube.com/",
        "whatsapp": "https://web.whatsapp.com/",
        "email": "https://mail.google.com/"
    }
    if app_name.lower() in apps:
        webbrowser.open(apps[app_name.lower()])
    else:
        os.system(f"start {app_name}")

def get_current_time() -> str:
    now = datetime.datetime.now()
    return f"The current time is {now.strftime('%I:%M %p')}"

def set_alarm(text: str = "") -> str:
    match = re.search(r"(\d{1,2})(?:[:.](\d{2}))?\s*(am|pm)?", text, re.IGNORECASE)
    if match:
        hour = int(match.group(1))
        minute = int(match.group(2)) if match.group(2) else 0
        period = match.group(3).lower() if match.group(3) else "am"
        return f"Alarm set for {hour}:{minute:02d} {period.upper()}."
    return "Please specify a time for the alarm."

def create_calendar_event(text: str = "") -> str:
    # Try to extract date, time, and title
    title_match = re.search(r"(?:called|about|named)\s+([a-zA-Z0-9\s]+)", text)
    date_match = re.search(r"on\s+([a-zA-Z]+\s+\d{1,2})", text)
    time_match = re.search(r"at\s+(\d{1,2})(?::(\d{2}))?\s*(am|pm)?", text, re.IGNORECASE)

    title = title_match.group(1).strip() if title_match else None
    date = date_match.group(1).strip() if date_match else None
    hour = int(time_match.group(1)) if time_match else None
    minute = int(time_match.group(2)) if time_match and time_match.group(2) else 0
    period = time_match.group(3).lower() if time_match and time_match.group(3) else "am"

    if not title:
        return "What should I name the event?"
    if not date:
        return f"On which date do you want to schedule '{title}'?"
    if not hour:
        return f"What time should I schedule '{title}' on {date}?"

    return f"Calendar event '{title}' created on {date} at {hour}:{minute:02d} {period.upper()}."