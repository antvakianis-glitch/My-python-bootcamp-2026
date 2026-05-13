from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

response = requests.get(URL, headers=headers)
data = response.text

print(response.status_code)
print("blocked" if "Robot Check" in data or "captcha" in data.lower() else "ok")

soup = BeautifulSoup(data, "html.parser")

try:
    whole = soup.find("span", class_="a-price-whole").getText().strip(".")
    fraction = soup.find("span", class_="a-price-fraction").getText()

    price = float(f"{whole}.{fraction}")
except AttributeError:
    print("Could not find price. Amazon may have blocked the request.")
    exit()

if price < 100:
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)

            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject: Instant Pot Duo Plus: Low Price Alert!\r\n\r\nThe current price is ${price}.\r\n")
        print("Email sent!")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your email/app password.")
    except smtplib.SMTPException as e:
        print(f"Email error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


