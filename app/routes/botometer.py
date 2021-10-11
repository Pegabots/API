from app import app
from flask import jsonify, request
from app.models.analises import Analises, AnaliseSchema
from app.twitter_handler import TwitterHandler
from app.models.botprobability import BotProbability
from app.services.botometer_service import BotometerService


@app.get("/catch")
def catch():
    handle = str(request.args.get('profile'))
    botometer_service = BotometerService()
    response = botometer_service.catch_service(handle)
    return response


@app.get('/botprobability')
def botProbability():
    p = BotProbability()
    return p.botProbability()

@app.get('/complete')
def complete():
    handle = str(request.args.get('profile'))
    result = Analises.query.filter_by(handle=handle).first()
    # result = Analises.query.get(1);
    analise_schema = AnaliseSchema()
    return jsonify(analise_schema.dump(result))

@app.post('/feedback')
def feedback():
    return jsonify("feedback")
