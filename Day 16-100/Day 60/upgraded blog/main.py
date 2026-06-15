from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("EMAIL")
my_password = os.getenv("PASSWORD")

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":

        user_name = request.form["name"]
        user_email = request.form["email"]
        user_phone = request.form["phone"]
        user_message = request.form["message"]

        print(f"Name: {user_name}\nEmail: {user_email}\nPhone: {user_phone}\nMessage: {user_message}")

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)

                email_message = f"Subject: New Blog Contact Message!\n\nName: {user_name}\nEmail: {user_email}\nPhone: {user_phone}\nMessage: {user_message}"

                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=my_email,
                    msg=email_message.encode('utf-8')
                )
            print("Email sent!")
        except smtplib.SMTPAuthenticationError:
            print("Authentication failed. Check your email/app password.")
        except smtplib.SMTPException as e:
            print(f"Email error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

        return render_template("contact.html", msg_sent=True)

    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":

    app.run(debug=True, port=5001)
