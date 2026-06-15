from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    current_date = datetime.datetime.now().year
    return render_template("index.html", date=current_date)


@app.route("/guess/<name>")
def guess(name):

    response = requests.get(f"https://api.agify.io?name={name}")
    data = response.json()
    current_name = data.get("name")
    current_age = data.get("age")

    g_response = requests.get(f"https://api.genderize.io?name={name}")
    g_data = g_response.json()
    current_gender = g_data.get("gender")
    return render_template("guess.html", name = current_name, age = current_age, gender = current_gender)

@app.route("/blog")
def get_blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)