import smtplib
import os
from email.message import EmailMessage

def send_email(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = os.getenv("SMTP_USER")
    msg['To'] = os.getenv("TO_EMAIL")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASS"))
        smtp.send_message(msg)

if __name__ == "__main__":
    send_email("Euromillions – Résultats analysés", "Vous avez gagné ! (ou pas 😅)")
