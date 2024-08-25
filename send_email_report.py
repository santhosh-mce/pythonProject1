import smtplib
from email.mime.multipart import MIMEMultipart  # Corrected import
from email.mime.text import MIMEText  # Corrected import
import schedule
import time
from datetime import datetime

# Email credentials and configuration
SMTP_SERVER = "smtp.gmail.com"  # e.g., Gmail's SMTP server
SMTP_PORT = 587
EMAIL_USER = "webdesign1507@gmail.com"
EMAIL_PASS = "guqb zdjw mcyf gtnn"  # Consider using environment variables for security
EMAIL_TO = "recipient_email@example.com"
EMAIL_SUBJECT = "Daily Report"


def send_email_1000_times():
    # Send the email 1,000 times
    for i in range(1000):
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = EMAIL_TO
        msg['Subject'] = EMAIL_SUBJECT

        # Email body
        body = f"Hello,\n\nThis is email number {i+1} sent on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.\n\nBest regards,\nYour Automation Script"
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Set up the SMTP server
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)

            # Send the email
            server.send_message(msg)
            server.quit()

            print(f"Email {i+1} sent successfully!")

        except Exception as e:
            print(f"Failed to send email {i+1}: {str(e)}")

if __name__ == "__main__":
    send_email_1000_times()