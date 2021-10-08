from app import app
from flask import jsonify
from app.models import Analises, AnaliseSchema

@app.get("/botometer/<handle>")
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
