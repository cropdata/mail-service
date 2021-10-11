from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *


def sendGridMail(from_email, to_emails, cc_emails, subject, body, api_key):
    """Sendgrid  mail service method"""

    personalization = Personalization()
    for email in to_emails:
        personalization.add_to(Email(email))
    for email in cc_emails:
        personalization.add_cc(Email(email))
    message = Mail(
        from_email=from_email,
        subject=subject,
        html_content=body)
    message.add_personalization(personalization)
    try:
        sendgrid_client = SendGridAPIClient(api_key=api_key)
        sendgrid_client.send(message)
    except Exception as e:
        print(e)


import smtplib
import ssl
from email.message import EmailMessage


def smtpMail(sender_email, receiver_email, password, message, subject=None, cc_email=None):
    port = 587
    smtp_server = 'smtp.gmail.com'
    msg = EmailMessage()
    msg.set_content(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Cc"] = cc_email

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.send_message(msg)

    except Exception as e:
        print(e)
