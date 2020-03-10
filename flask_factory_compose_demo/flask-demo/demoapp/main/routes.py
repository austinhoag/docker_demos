from flask import Blueprint

main = Blueprint('main',__name__)

@main.route("/") 
def base(): 
	return "home"