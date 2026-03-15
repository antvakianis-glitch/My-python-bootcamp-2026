import requests
import html
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

TWELVE_DATA_KEY = os.environ.get("TWELVE_DATA_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.environ.get("TWILIO_PHONE")
MY_PHONE = os.environ.get("MY_PHONE")

def calc_percent(yest, bef):
    diff = yest - bef
    per_diff = (diff / bef) * 100
    if diff > 0:
        up_down = "🔺"
    elif diff < 0:
        up_down = "🔻"
    else:
        up_down = "➖"
    return per_diff, up_down


parameters = {
    "symbol": STOCK,
    "interval": "1day",
    "outputsize": 2,
    "apikey": TWELVE_DATA_KEY
}

try:
    response = requests.get("https://api.twelvedata.com/time_series",params=parameters)
    response.raise_for_status()
    data = response.json()

    if "status" in data and data["status"] == "error":
        print(f"❌ API Error: {data.get('message', 'Unknown error')}")
        exit()

    values = data["values"]

    yesterday_data = float(values[0]["close"])
    day_before_data = float(values[1]["close"])

    percent_diff,icon = calc_percent(yesterday_data,day_before_data)

    print(f"{STOCK} Movement: {icon}{percent_diff:.2f}%")
    print(f"Yesterday: ${yesterday_data:.2f}")
    print(f"Day Before: ${day_before_data:.2f}")

    if abs(percent_diff) >= 0.5:
        print("\n🚨 Significant movement! Fetching news...")

        news_parameters = {
            "apiKey":NEWS_API_KEY,
            "q": "Tesla Inc",
            "sortBy": "publishedAt",
            "pageSize": 3,
            "language": "en"
        }
        news_response = requests.get("https://newsapi.org/v2/everything",params=news_parameters)

        news_response.raise_for_status()
        articles = news_response.json()["articles"]

        headlines = [
            f"• {html.unescape(article['title'][:70])}"  # ← Πρώτοι 70 χαρακτήρες
            for article in articles[:2]
        ]

        news_text = (
                f"{STOCK}: {icon}{abs(percent_diff):.2f}%\n\n"
                "Top news:\n" +
                "\n".join(headlines)
        )

        print("=" * 60)
        print(news_text)
        print(f"\nMessage length: {len(news_text)} characters")
        print("=" * 60)

        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=news_text,
            from_=TWILIO_PHONE,
            to=MY_PHONE
        )
        print(f"SMS Sent! Status: {message.status}")
    else:
        print(f"Movement ({percent_diff:.2f}%) is lower than 5%. No alert sent.")

except Exception as e:
    print(f"Error: {e}")

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

