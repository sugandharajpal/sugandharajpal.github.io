from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# SMTP settings
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER = 'sugandha.rajpal@gmail.com'
SMTP_PASSWORD = 'ylmczixytptendly'

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    name = data['name']
    email = data['email']
    message_content = data['message']

    message = MIMEText(f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_content}")
    message['Subject'] = f'New Contact Form Message from {name}'
    message['From'] = SMTP_USER
    message['To'] = SMTP_USER  # You send to yourself

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, SMTP_USER, message.as_string())
        server.quit()
        return jsonify({'message': 'Email sent successfully!'}), 200
    except Exception as e:
        return jsonify({'message': f'Failed to send email: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
