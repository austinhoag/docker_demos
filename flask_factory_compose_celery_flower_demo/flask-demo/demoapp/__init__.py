from flask import Flask
from celery import Celery
import redis


cel = Celery(__name__,broker='redis://redis:6379/0',
			backend='redis://redis:6379/0')

def create_app():
	""" Create the flask app instance"""
	app = Flask(__name__)
	# cel.conf.update(app.config)

	from demoapp.main.routes import main

	app.register_blueprint(main)

	return app