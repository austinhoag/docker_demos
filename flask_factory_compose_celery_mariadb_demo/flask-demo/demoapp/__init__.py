from flask import Flask
from celery import Celery

import os

user = os.environ['DJ_DB_USER']
password = os.environ['DJ_DB_PASS']
backend_connection_str = f'db+mysql+pymysql://{user}:{password}@datajoint00.pni.princeton.edu:3306/ahoag_celery_test?ssl_ca=/etc/ssl/certs/ca-certificates.crt'

cel = Celery(__name__,broker='redis://redis:6379/0',
			backend=backend_connection_str)

def create_app():
	""" Create the flask app instance"""
	app = Flask(__name__)
	# cel.conf.update(app.config)

	from demoapp.main.routes import main

	app.register_blueprint(main)

	return app