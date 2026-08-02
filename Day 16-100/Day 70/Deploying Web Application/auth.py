from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from models import db, User
from forms import RegisterForm, LoginForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('auth.login'))

        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )

        new_user = User(
            name=form.name.data,
            email=form.email.data,
            password=hash_and_salted_password
        )
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for("main.get_all_posts"))

    return render_template("register.html", form=form)


@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('auth.login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('auth.login'))
        else:
            login_user(user)
            return redirect(url_for("main.get_all_posts"))

    return render_template("login.html", form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.get_all_posts'))