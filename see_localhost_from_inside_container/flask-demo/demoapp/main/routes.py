from flask import Blueprint
import requests
import logging
import subprocess
main = Blueprint('main',__name__)

logging.basicConfig(level=logging.DEBUG)
@main.route("/") 
def base(): 
	return "home"

@main.route("/test") 
def test(): 
	task = subprocess.Popen("ip route | awk 'NR==1 {print $3}'", shell=True, stdout=subprocess.PIPE)
	data = task.stdout.read()
	localhost_addr = data.decode('utf-8').strip('\n')
	logging.debug("localhost address:")
	logging.debug(localhost_addr)
	response = requests.get(f'http://{localhost_addr}:5005/')
	logging.debug("Response is:")
	logging.debug(response.txt)
	return "test"