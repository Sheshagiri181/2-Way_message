import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

sender_email = "--------"
password = "------------"  
receiver_email ="------------"
cc_email = "---------------"
subject = "Test Email"
body = "Hello, this is a test email sent."

# Compose the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Cc"] = cc_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

filename = "111.png"  
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={filename}")
    message.attach(part)

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, password)
        server.sendmail(sender_email, [receiver_email] + [cc_email], message.as_string())
        print("Email sent successfully!")
except Exception as e:
    print("Error sending email:", e)
