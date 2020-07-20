from flask import Blueprint
import os
import requests

main = Blueprint('main',__name__)

@main.route("/") 
def base(): 
	return "home"

@main.route("/test") 
def test(): 
	d='/jukebox/LightSheetData/lightserv_testing/apptest3'
	os.mkdir(d)
	return f"Made directory: {d}"

@main.route("/launchcv",methods=['GET']) 
def launchcv(): 
	response = requests.get('http://flask-cvlauncher:5005/ngdemo')
	print(response)
	print(response.text)
	return f"Sent GET request to flask-cvlauncher:5005/ngdemo"

@main.route("/send_data") 
def send_data(): 
	response = requests.post('http://flask-cvlauncher:5005/dest',json={"mykey":"myval"})
	return f"Sent POST request to flask-cvlauncher:5005/dest"