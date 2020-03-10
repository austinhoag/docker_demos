from flask import Flask
from celery import Celery
import redis
from datetime import timedelta

cel = Celery(__name__,broker='redis://redis:6379/0',
			backend='redis://redis:6379/0')

celery_beat_schedule = {
    'test_schedule': {
        'task': 'demoapp.main.routes.my_background_task',
        'schedule': timedelta(seconds=3)
    },
}

def create_app():
	""" Create the flask app instance"""
	app = Flask(__name__)

	app.config['CELERYBEAT_SCHEDULE'] = celery_beat_schedule
	cel.conf.update(app.config)

	from demoapp.main.routes import main

	app.register_blueprint(main)

	return app

