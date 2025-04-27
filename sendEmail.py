import smtplib
from email.mime.text import MIMEText

# SMTP Server Configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER = 'sugandha.rajpal@gmail.com'
SMTP_PASSWORD = 'ylmczixytptendly'  # Use App Password, NOT your Gmail login password

# Email Content
subject = 'Test Email from Python'
body = 'This is a plain text email sent from Python backend!'
sender_email = 'sugandha.rajpal@gmail.com'
receiver_email = 'thesunilyoga@gmail.com'

# Create the email
message = MIMEText(body, 'plain')
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Connect to the SMTP server and send email
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Upgrade the connection to secure
    server.login(SMTP_USER, SMTP_PASSWORD)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print('Email sent successfully!')
except Exception as e:
    print(f'Error sending email: {e}')
finally:
    server.quit()
