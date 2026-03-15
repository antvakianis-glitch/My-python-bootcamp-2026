import smtplib
import datetime as dt
import random

with open("quotes.txt", encoding="utf-8") as file:
    all_quotes = file.readlines()
    quote_text = random.choice(all_quotes).strip()

current_date = dt.datetime.now().weekday()

if current_date == 0:

    my_email = "pythontony6@gmail.com"
    my_password = "fkujgxrydtbqpvxo"

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)

        connection.sendmail(from_addr=my_email,to_addrs="pythontony7@yahoo.com",
                            msg=f"Subject: Have a good Monday\n\n{quote_text}")
