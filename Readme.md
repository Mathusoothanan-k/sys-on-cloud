<!-- ABOUT THE PROJECT -->
# About The Project

Ngrok SSH Automation Script for sys on cloud in linux

This Python script automates the process of capturing an ngrok SSH tunnel URL from a screenshot, extracting the relevant SSH connection details using OCR (Optical Character Recognition), and sending these details via email.

### Prerequisites

*  Python 3.x
* `psutil` library
* `subprocess` module (part of Python standard library)
* `time` module (part of Python standard library)
* `os` module (part of Python standard library)
* `pytesseract` library
* `Pillow` library
* `smtplib` library (part of Python standard library)
* `email` library (part of Python standard library)
* `ngrok` installed and accessible in your PATH
* `scrot` utility installed (for taking screenshots)

### OS Support

- [x] Linux 
 - [ ]  Windows
 - [ ]  Mac ISO
    
### Enable Two-Factor Authentication (2FA) For Gmail purpose

Ensure that two-factor authentication is enabled for your Google account. If it's not already enabled, follow these steps:

1. Go to your [Google Account](https://myaccount.google.com/).
2. Select "Security" from the left-hand menu.
3. Under "Signing in to Google," select "2-Step Verification" and follow the on-screen instructions to set it up.

### Generate an App Password

Once 2FA is enabled, you can generate an app-specific password for use in your script:

1. Go to the [App passwords](https://myaccount.google.com/apppasswords) page in your Google account.
2. Enter a name for the app password, such as "Python Email Script."
3. Click "Generate."
4. Google will display a 16-character app password. Make sure to copy it and store it securely as you will need it in your script.

By following these steps, you'll enhance the security of your Google account while allowing your Python script to send emails programmatically.
        
### Usage

1. Start the ssh service 
2. Update the script with your email credentials:
    ```python
    sender_email = '[xxxxxxxxxxxxx]YOUR_EMAIL@gmail.com'
    app_password = '[xxxxxxxxxxxxx]YOUR_APP_PASSWORD'
    receiver_email = '[xxxxxxxxxxxxxx]RECEIVER_EMAIL@gmail.com'
    ```

3. Run the script:
    ```sh
    python script_name.py
    ```
### NGROK Service connection

1. Sign up for an ngrok account if you don't have one: [ngrok Sign Up](https://dashboard.ngrok.com/signup).
2. Log in to your ngrok dashboard: [ngrok Dashboard](https://dashboard.ngrok.com).
3. Copy your authtoken from the dashboard.
4. Run the following command to add your authtoken:
    ```sh
    ngrok authtoken YOUR_AUTHTOKEN
    ```
### Documentations
- [Ngrok Documentation](https://ngrok.com/docs)
- [Ngrok Support](https://ngrok.com/support)

### Script Details

- **extract_text_from_image(image_path):** 
  This function takes the path of an image, uses Tesseract to extract text from it, and returns the extracted text.

- **send_email(sender_email, app_password, receiver_email, subject, result):**
  This function sends an email with the specified subject and message body. It uses Gmail's SMTP server to send the email.

- **Main Process:**
  1. Start ngrok to create an SSH tunnel.
  2. Capture the current window screenshot containing the ngrok URL using `scrot`.
  3. Extract the SSH connection details from the screenshot using OCR.
  4. Save the extracted text to a file.
  5. Parse the required port number from the saved text file.
  6. Construct the SSH command using the extracted port number.
  7. Send an email with the SSH command to the specified recipient.

### Example Output

The script sends an email with the SSH command, for example:
```
ssh kali@0.tcp.in.ngrok.io -p xxxxx
```

### Notes

- Ensure that `ngrok` is properly configured and authenticated on your system.
- Make sure to use an app-specific password for sending emails if you are using Gmail and have 2-step verification enabled.
- Modify the sleep durations (`time.sleep()`) if necessary to ensure proper timing between commands.
