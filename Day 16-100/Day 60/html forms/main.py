from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def receive_data():
    username = request.form["username"]
    password = request.form["password"]
    return f"<h1>Username: {username}</h1><h1>Password: {password}</h1>"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
