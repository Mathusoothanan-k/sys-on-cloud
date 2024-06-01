import psutil
import subprocess
import time
import os
import pytesseract
from PIL import Image
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def extract_text_from_image(image_path):
    with Image.open(image_path) as img:
        extracted_text = pytesseract.image_to_string(img)
        
        return extracted_text
        
def send_email(sender_email, app_password, receiver_email, subject, result):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(result, 'plain'))

  
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  
        server.login(sender_email, app_password)  # Log in with the app password
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
        
if __name__ == "__main__":
    os.system('ngrok tcp 22 &')
    time.sleep(15)
    ngrok = "ngrok_ssh.png"
    subprocess.run(["scrot", "-u", "-o",ngrok])
    
    extracted_text = extract_text_from_image(ngrok)
    with open('sample.txt', 'w') as file:
        file.write(extracted_text)
    time.sleep(6)
    command = "grep 'tcp.in.ngrok.io' sample.txt | cut -d':' -f3 | cut -d' ' -f1"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

   
    port = result.stdout.strip()
    output = f"ssh kali@0.tcp.in.ngrok.io -p {port}"

    sender_email = 'XXXXXXXXXXXXXXX'
    app_password = 'XXXXXXXXXXXXXX'
    receiver_email = 'XXXXXXXXXXXX'
    subject = 'SSH key'
    send_email(sender_email, app_password, receiver_email, subject, output)

    
