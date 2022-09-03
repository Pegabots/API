from flask import Blueprint, render_template
from flask import jsonify, request

from app.models.models import Analises, AnaliseSchema
from app.services.botometer_service import BotometerService

router = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth",
    template_folder="templates"
)

@router.get("/login")
def login():
    return render_template(
        "login.html",
    )

@router.get("/register")
def register():
    return render_template(
        "register.html"
    )