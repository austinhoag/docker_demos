from flask import Flask

def create_app():
	""" Create the flask app instance"""
	
	app = Flask(__name__)
	# cel.conf.update(app.config)

	from demoapp.main.routes import main

	app.register_blueprint(main)

	return app