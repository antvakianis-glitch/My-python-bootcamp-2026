import requests
from datetime import datetime, timezone
import smtplib
import os
from tkinter import *
from dotenv import load_dotenv

load_dotenv()

window = Tk()
window.title("ISS Tracker")

MY_LAT = 45.405906
MY_LONG = 19.989177
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

def check_is_overhead(lat,lon):
    return abs(lat - MY_LAT) <= 5 and abs(lon - MY_LONG) <= 5

def check_is_dark(now,s_rise,s_set):
    return now > s_set or now < s_rise

def check_iss_status():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now(timezone.utc).hour

    if check_is_overhead(iss_latitude,iss_longitude) and check_is_dark(time_now,sunrise,sunset):

        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)

            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject: Iss Overhead!\n\nThe Iss is passing overhead now")
        print("Email sent!")

    else:

        print(f"Checking... ISS is at {iss_latitude}, {iss_longitude}. Not overhead yet.")

    window.after(60000, func=check_iss_status)

check_iss_status()

window.mainloop()




