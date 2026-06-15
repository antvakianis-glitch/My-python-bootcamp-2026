from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
all_posts = response.json()


app = Flask(__name__)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in all_posts:
        if int(blog_post["id"]) == int(index):
            requested_post = blog_post

    if requested_post is None:
        return "Post not found", 404

    return render_template("post.html",
                               current_post=requested_post,
                               page_title=requested_post["title"],
                               bg_image="assets/img/post-bg.jpg")

@app.route("/")
def home():
    return render_template("index.html",page_title="Antonios Blog", bg_image="assets/img/mypic.jpg", posts=all_posts)

@app.route('/about')
def about_page():
    return render_template("about.html",page_title="About Me", bg_image="assets/img/about-bg.jpg")

@app.route('/contact')
def contact_page():
    return render_template("contact.html",page_title="Contact Me", bg_image="assets/img/contact-bg.jpg")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')