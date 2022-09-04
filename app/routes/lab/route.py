from datetime import date, datetime, timedelta
from crypt import methods
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask import jsonify, request
from flask_login import current_user, login_required, logout_user
import json

from app.models import db
from app.services.twitter_handler import TwitterHandler
from app.services.botometer_service import BotometerService
from app.models.models import BotProbability, Analises, AnaliseSchema, AnalisesGroup
from app.routes.lab.forms import AnaliseForm

router = Blueprint(
    "lab",
    __name__,
    url_prefix="/lab",
    template_folder="templates"
)

@router.route("/home", methods=["GET", "POST"])
@login_required
def home():
    def _getUser(user_data):        
        user = [{
            "created_at": user_data["created_at"],
            "default_profile": user_data["default_profile"],
            "description": user_data["description"],
            "followers_count": user_data["followers_count"],
            "friends_count": user_data["friends_count"],
            "handle": user_data["screen_name"],
            "lang": user_data["lang"],
            "location": user_data["location"],
            "name": user_data["name"],
            "profile_image": user_data["profile_image_url"],
            "twitter_id": user_data["id"],
            "twitter_is_protected": user_data["protected"],
            "verified": user_data["verified"],
            "withheld_in_countries": user_data["withheld_in_countries"],
            "É Bot?": ''
        }]

        return(user)

    form = AnaliseForm()
    analises = None

    if form.validate_on_submit():
        analises_group = AnalisesGroup(
            user=current_user.id,
            term=form.handle.data
        )
        db.session.add(analises_group)
        db.session.commit()

        handler = TwitterHandler(
            user=current_user
        )
        botometer = BotometerService()
        pegabot = BotProbability()

        data = handler.searchTweets(
            q=form.handle.data, 
            num_tweets=20,
        )
        analises = []

        for item in data:
            user = item._json["user"]

            user_hist = botometer.findUserAnalisisByHandle(
                user["screen_name"]
            )

            if "id" in user_hist:
                analises.append(user_hist)
            else:
                user_tl = handler.getUserTimeline(
                    user["id"]
                )

                if 'api_errors' in user_tl: 
                    # Fri Dec 10 00:43:39 +0000 2021
                    created_datetime = datetime.strptime(
                        user["created_at"],
                        "%a %b %d %H:%M:%S %z %Y"
                    )
                    if(date.today() == created_datetime):
                        print("Account created today")
                        # return {'api_errors': [{'code': '11', 'message:': 'Account created today.'}], 'codes': '11', 'reason': 'Too litle information available', 'args': 'Account created today.'}
                    # return user_tl
                
                probability = pegabot.botProbability(
                    str.lower(user["screen_name"]),
                    user_tl,
                    _getUser(user)
                )
                analise = Analises(
                    group=analises_group.id,
                    # User
                    handle = user["screen_name"],
                    twitter_id = user["id"],
                    twitter_handle = str.lower(user["screen_name"]),
                    twitter_user_name = user["name"],
                    twitter_is_protected = user["protected"],
                    twitter_user_description = user["description"],
                    twitter_followers_count = user["followers_count"],
                    twitter_friends_count = user["friends_count"],
                    twitter_location = user["location"],
                    twitter_is_verified = user["verified"],
                    twitter_lang = user["lang"],
                    twitter_created_at = Analises.process_bind_param(value=user["created_at"]),
                    twitter_default_profile = user["default_profile"],
                    twitter_profile_image = user["profile_image_url"],
                    # twitter_withheld_in_countries = response.twitter_withheld_in_countries, # giving error, needs a refactor
                    total = probability.total,
                    cache_times_served = 0, #
                    cache_validity = datetime.today() + timedelta(30),
                    pegabot_version = probability.pegabot_version,
                )
                db.session.add(analise)
                db.session.commit()
                analise_schema = AnaliseSchema()
                analises.append(
                    analise_schema.dump(analise)
                )

        return redirect("/lab/analises/%s" % analises_group.id)

    user_analises_groups = AnalisesGroup.query.filter_by(
        user=current_user.id
    )
    
    return render_template(
        "home.html",
        current_user=current_user,
        form=form,
        analises=analises,
        user_analises_groups=user_analises_groups
    )

@router.route("/analises/<group_id>", methods=["GET"])
@login_required
def view_analises(group_id):
    try:
        group = AnalisesGroup.query.filter_by(
            id=group_id
        ).first()
        analises = Analises.query.filter_by(
            group=group_id
        )
    except:
        flash("Pesquisa não encontrada")
        return redirect(url_for("lab.home"))
    
    user_analises_groups = AnalisesGroup.query.filter_by(
        user=current_user.id
    )

    return render_template(
        "analises.html",
        current_user=current_user,
        analises=analises,
        term=group.term,
        user_analises_groups=user_analises_groups
    )