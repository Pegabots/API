from app import app, celery, Celery
from flask import jsonify, request, url_for
from app.models.models import Analises, AnaliseSchema, BotProbability
from app.services.botometer_service import BotometerService


@app.get("/catch")
def catch():
    handle = str(request.args.get('profile'))
    botometer_service = BotometerService()
    response = botometer_service.catch(handle)
    return jsonify(response), 200


@app.get('/botprobability') # test only
def botprobability():
    h = str(request.args.get('profile'))
    bp = BotProbability()
    task = bp.botProbability.apply_async(countdown=60)
    return jsonify({}), 202, {'Location': url_for('taskstatus',
                                                  task_id=task.id)}



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

########## TASKS #########

@app.route('/status/<task_id>')
def taskstatus(task_id):
    # bp = ()
    task = BotProbability.botProbability.AsyncResult(task_id)
    if task.state == 'PENDING':
        # job did not start yet
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)