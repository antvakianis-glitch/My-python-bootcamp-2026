from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    requested_post = next((p for p in all_posts if p["id"] == post_id), None)
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
