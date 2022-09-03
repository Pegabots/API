from flask import Blueprint
from flask import jsonify, request

from app.models.models import Analises, AnaliseSchema
from app.services.botometer_service import BotometerService

router = Blueprint(
    "analise",
    __name__
)

@router.get("/catch")
def catch():
    handle = str(request.args.get('profile'))
    botometer_service = BotometerService()
    response = botometer_service.catch(handle)
    return jsonify(response), 200


@router.get('/botprobability') # test only
def botprobability():
    handle = str(request.args.get('profile'))
    botometer_service = BotometerService()
    response = botometer_service.botProbability(handle)
    return jsonify(response), 200

@router.get('/complete')
def complete():
    handle = str(request.args.get('profile'))
    result = Analises.query.filter_by(handle=handle).first()
    # result = Analises.query.get(1);
    analise_schema = AnaliseSchema()
    return jsonify(analise_schema.dump(result))

@router.post('/feedback')
def feedback():
    return jsonify("feedback")
