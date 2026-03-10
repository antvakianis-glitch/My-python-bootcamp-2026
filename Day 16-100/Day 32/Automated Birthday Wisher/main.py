import datetime as dt
import pandas
import random
import smtplib
from tkinter import messagebox
import os
from dotenv import load_dotenv

try:
    data = pandas.read_csv("birthdays.csv")
    data_dict = data.to_dict(orient="records")
except FileNotFoundError:
    messagebox.showerror("Error", "The birthdays.csv file does not exist")

else:
    now = dt.datetime.now()
    current_date = (now.month, now.day)

    birthday_people = [person for person in data_dict if (person["month"], person["day"]) == current_date]

    if birthday_people:
        messagebox.showinfo(title="Success!", message=f"Found {len(birthday_people)} birthday(s) today!")

        load_dotenv()

        MY_EMAIL = os.environ.get("MY_EMAIL")
        MY_PASSWORD = os.environ.get("MY_PASSWORD")

        if not MY_EMAIL or not MY_PASSWORD:
            messagebox.showerror("Error", "Missing credentials in .env file!")
            exit()

        sent_to = []

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)

                for person in birthday_people:
                    random_numb = random.randint(1, 3)
                    try:
                        with open(f"./letter_templates/letter_{random_numb}.txt", "r", encoding="utf-8") as file:
                            template = file.read()
                    except FileNotFoundError:
                        messagebox.showerror("Error", f"The letter_{random_numb}.txt does not exist")
                        continue

                    letter_to_send = template.replace("[NAME]", person["name"])
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=person["email"],
                        msg=f"Subject: Happy Birthday!\n\n{letter_to_send}"
                    )
                    sent_to.append(person['name'])


            if sent_to:
                names = "\n".join(sent_to)
                messagebox.showinfo(title="Success!",message=f"✓ Sent birthday emails to:\n{names}")

        except smtplib.SMTPException as e:
            messagebox.showerror("Email Error", f"Failed to send email: {e}")
    else:
        messagebox.showinfo(title="No Birthdays", message="No birthdays today.")








