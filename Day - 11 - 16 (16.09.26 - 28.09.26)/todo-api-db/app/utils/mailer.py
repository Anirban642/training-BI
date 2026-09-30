import base64
import logging

import mailtrap as mt
from app.config.config import (
    MAIL_SENDER_EMAIL,
    MAIL_SENDER_NAME,
    MAILTRAP_INBOX_ID,
    MAILTRAP_TOKEN,
)
from app.utils.filename import export_filename

logger = logging.getLogger(__name__)


def send_welcome_email(to_email: str, username: str):
    if not MAILTRAP_TOKEN:
        return

    mail = mt.Mail(
        sender=mt.Address(email=MAIL_SENDER_EMAIL, name=MAIL_SENDER_NAME),
        to=[mt.Address(email=to_email)],
        subject="Welcome to Todo App!",
        text=f"Hi {username},\n\nWelcome to our platform. Start organizing your tasks easily!",
    )
    try:
        client = mt.MailtrapClient(
            token=MAILTRAP_TOKEN, sandbox=True, inbox_id=MAILTRAP_INBOX_ID
        )
        client.send(mail)
    except Exception:
        logger.exception("Welcome email failed for %s", to_email)


def send_todos_export_email(to_email: str, username: str, json_content: str):
    if not MAILTRAP_TOKEN:
        return

    encoded_file = base64.b64encode(json_content.encode("utf-8"))

    mail = mt.Mail(
        sender=mt.Address(email=MAIL_SENDER_EMAIL, name=MAIL_SENDER_NAME),
        to=[mt.Address(email=to_email)],
        subject="Your Exported Todos",
        text=f"Hi {username},\n\nPlease find attached the JSON export of your todos.",
        attachments=[
            mt.Attachment(
                content=encoded_file,
                filename=export_filename(username),
                mimetype="application/json",
                disposition="attachment",
            )
        ],
    )
    try:
        client = mt.MailtrapClient(
            token=MAILTRAP_TOKEN, sandbox=True, inbox_id=MAILTRAP_INBOX_ID
        )
        client.send(mail)
    except Exception:
        logger.exception("Todos export email failed for %s", to_email)