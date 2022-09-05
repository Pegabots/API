from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class AnaliseForm(FlaskForm):
    handle = StringField(
        "Termo",
    )
    submit = SubmitField("Analisar")