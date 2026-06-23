import smtplib
from email.message import EmailMessage

from config import (
    EMAIL_SENDER,
    EMAIL_RECEIVER,
    EMAIL_PASSWORD,
)


def send_email(subject: str, body: str):
    message = EmailMessage()

    message["Subject"] = subject
    message["From"] = EMAIL_SENDER
    message["To"] = EMAIL_RECEIVER

    message.set_content(body)

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:

        smtp.login(
            EMAIL_SENDER,
            EMAIL_PASSWORD
        )

        smtp.send_message(message)