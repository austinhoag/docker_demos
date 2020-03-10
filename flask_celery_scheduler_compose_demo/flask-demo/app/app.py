# app.py - a minimal flask application
from flask import Flask
from celery import Celery
import redis
from datetime import timedelta

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://redis:6379/0' #
app.config['CELERY_RESULT_BACKEND'] = 'redis://redis:6379/0'
celery_beat_schedule = {
    'test_schedule': {
        'task': 'app.my_background_task',
        'schedule': timedelta(seconds=3)
    },
}
app.config['CELERYBEAT_SCHEDULE'] = celery_beat_schedule

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@app.route("/")
def base():
	return "Hello Worlds"

@celery.task
def my_background_task():
    # some long running task here
    return "test task complete"

@app.route("/test_celery")
def test_celery():
	task = my_background_task.delay()
	result = task.get()
	print(result)
	print(type(result))
	return "Test success"

@app.route("/show_redis")
def show_redis():
	kv = redis.Redis(host="redis", decode_responses=True)
	# keys = kv.keys("*")
	result = kv.mget('celery')
	print(result)
	print()
	# print(kv.get('celery'))
	return "done"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')