import os
from datetime import date
import hashlib
import requests
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from dotenv import load_dotenv

# Import από τα νέα δικά μας αρχεία
from models import db, User, BlogPost
from auth import auth_bp
from posts import posts_bp

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

# Gravatar filter setup
def gravatar_url(email, size=100, rating='g', default='retro', force_default=False):
    hash_value = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    return f"https://www.gravatar.com/avatar/{hash_value}?s={size}&d={default}&r={rating}"

app.jinja_env.filters['gravatar'] = gravatar_url

# Extensions
ckeditor = CKEditor(app)
Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# Database Setup
db_url = os.environ.get('DATABASE_URL', 'sqlite:///posts.db')
if db_url and db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "pool_pre_ping": True,
    "pool_recycle": 300,
}

db.init_app(app)

# --- REGISTER BLUEPRINTS ---
app.register_blueprint(auth_bp)
app.register_blueprint(posts_bp)

with app.app_context():
    db.create_all()

@app.context_processor
def inject_year():
    return dict(year=date.today().year)

# General Routes
@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

MAIL_ADDRESS = os.environ.get("EMAIL_KEY")

def send_email(name, email, phone, message):
    api_key = os.environ.get("RESEND_API_KEY")
    url = "https://api.resend.com/emails"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "from": "onboarding@resend.dev",
        "to": [MAIL_ADDRESS],
        "subject": "New Message from Blog",
        "html": f"<p><b>Name:</b> {name}</p><p><b>Email:</b> {email}</p><p><b>Phone:</b> {phone}</p><p><b>Message:</b> {message}</p>"
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code != 200:
            print(f"Resend API error: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Failed to send request: {e}")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True, port=5002)