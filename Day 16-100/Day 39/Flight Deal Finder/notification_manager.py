import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client

class NotificationManager:
    def __init__(self):
        self.twilio_sid = os.environ.get("TWILIO_SID")
        self.twilio_token = os.environ.get("TWILIO_AUTH_TOKEN")
        self.twilio_phone = os.environ.get("TWILIO_PHONE")
        self.my_phone = os.environ.get("MY_PHONE")  # Το δικό σου κινητό στο .env
        self.client = Client(self.twilio_sid, self.twilio_token)

        self.MY_EMAIL = os.environ.get("MY_EMAIL")
        self.MY_PASSWORD = os.environ.get("MY_PASSWORD")

    def send_email(self, price_amount, city_dest, airline, flight_type=None, layover_info=None, booking_url=None):
        """Send flight deal alert email"""

        # Email subject
        subject = f"✈️ Low Price Alert! Flight to {city_dest} - {price_amount}€"

        # Build email body
        body = f"""
    🎉 Great news! We found a cheap flight to {city_dest}!

    💰 Price: {price_amount}€
    ✈️  Airline: {airline}
    """

        # Add flight type if provided
        if flight_type:
            body += f"🛫 Flight Type: {flight_type}\n"

        # Add layover info if provided
        if layover_info:
            body += f"\n📍 Layover Details:\n{layover_info}\n"

        # Add booking link if provided
        if booking_url:
            body += f"\n🔗 Book now:\n{booking_url}\n"

        body += """
    ⚠️  Prices change quickly - book as soon as possible!

    Happy travels! 🌍✨
    """

        # Create email message
        msg = MIMEMultipart()
        msg['From'] = self.MY_EMAIL
        msg['To'] = self.MY_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send email
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.MY_EMAIL, self.MY_PASSWORD)
                server.send_message(msg)
            print("📧 Email sent successfully")
        except Exception as e:
            print(f"❌ Failed to send email: {e}")

