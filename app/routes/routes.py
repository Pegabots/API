from app import app
from flask import jsonify, request
from app.models.models import Analises, AnaliseSchema
from app.services.botometer_service import BotometerService
from concurrent.futures import ThreadPoolExecutor

@app.get("/catch")
def catch():
    handle = str(request.args.get('profile'))
    botometer_service = BotometerService()
    response = botometer_service.catch(handle)
    return jsonify(response), 200


@app.get('/botprobability') # test only
def botprobability():
    handle = str(request.args.get('profile'))
    botometer_service = BotometerService()
    response = botometer_service.botProbability(handle)
    return jsonify(response), 200

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

@app.get('/multicatches')
def multicatches():
    handle = str(request.args.get('profiles'))
    users = handle.split(',')

    results = list()
    for user in users:
        botometer_service = BotometerService()
        response = botometer_service.catch(user)
        results.append(response)

    return jsonify(results), 200

@app.get('/multicatchesparallel')
def multicatches2():
    handle = str(request.args.get('profiles'))
    users = handle.split(',')
    results = list()

    def getResult(username):
        botometer_service = BotometerService()
        response = botometer_service.catch(username)
        results.append(response)

    with ThreadPoolExecutor(max_workers=10) as pool:
        pool.map(getResult, users)

    return jsonify(results), 200
