from flask import Blueprint

main = Blueprint('main',__name__)

@main.route("/") 
def base(): 
	return "home"

@main.route("/test") 
def test(): 
	return "test"