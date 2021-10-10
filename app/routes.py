from app import app
from flask import jsonify, request
from app.models import Analises, AnaliseSchema
from app.tp import api, getUserTimeline, getDataFromUserByTwiiterHandle as findByHandle

@app.get("/")
@app.get("/botometer")
def botometer():
    handle = request.args.get('profile')
    user = findByHandle(handle)
    timeline = getUserTimeline(user.twitter_id_str, num_tweets=5)
    return jsonify({'user': user, 'timeline':timeline})
    # user = Analises.query.filter_by(handle=handle).first()
    # user = Analises.query.get(1)
    # print(f'{user}')
    analise_schema = AnaliseSchema()
    return jsonify(analise_schema.dump(user))

def botometer(handle):
    user = Analises.query.filter_by(handle=handle).first()
    # user = Analises.query.get(1)
    print(f'{user}')
    analise_schema = AnaliseSchema()
    return jsonify(analise_schema.dump(user))

@app.get('/complete')
def complete():
    return jsonify("analise completa")

@app.post('/feedback')
def feedback():
    return jsonify("feedback")
