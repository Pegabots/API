from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask import jsonify, request
from flask_login import current_user, login_user

from app import login_manager
from app.routes.auth.forms import SignupForm, LoginForm
from app.models.auth import User
from app.models import db

router = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth",
    template_folder="templates"
)

@router.route("/login", methods=["GET", "POST"])
def login():
    """
    Log-in page for registered users.

    GET requests serve Log-in page.
    POST requests validate and redirect user to dashboard.
    """
    # Bypass if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for("lab.home"))

    form = LoginForm()
    # Validate login attempt
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page or url_for("lab.home"))
        flash("Invalid username/password combination")
        return redirect(url_for("auth.login"))
    return render_template(
        "login.html",
        form=form,
        title="Log in.",
        template="login-page",
        body="Log in with your User account.",
    )

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in upon page load."""
    if user_id is not None:
        try:
            return User.query.get(user_id)
        except:
            return None
    return None

@router.route("/signup", methods=["GET", "POST"])
def signup():
    """
    User sign-up page.

    GET requests serve sign-up page.
    POST requests validate form & user creation.
    """
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            user = User(
                name=form.name.data, 
                email=form.email.data,
                twitter_api_key=form.twitter_api_key.data,
                twitter_api_secret=form.twitter_api_secret.data,
                twitter_access_token=form.twitter_access_token.data,
                twitter_access_token_secret=form.twitter_access_token_secret.data
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()  # Create new user
            
            return redirect(url_for("auth.login"))
        flash("A user already exists with that email address.")
    return render_template(
        "signup.html",
        title="Create an Account.",
        form=form,
        template="signup-page",
        body="Sign up for a user account.",
    )
