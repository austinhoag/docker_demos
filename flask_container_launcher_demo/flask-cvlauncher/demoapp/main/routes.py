from flask import Blueprint,request
import os
import docker
import secrets
import logging

logging.basicConfig(level=logging.DEBUG)


main = Blueprint('main',__name__)

@main.route("/") 
def base(): 
	return "home of flask-cvlauncher!@"

@main.route("/ngdemo") 
def ngdemo(): 
	client = docker.DockerClient(base_url='unix://var/run/docker.sock')
	session_name = secrets.token_hex(6)
	cv1_container_name = f'{session_name}_cv_container'
	cv1_name = f"test_cv"
	layer1_type = "segmentation"
	cv1_localhost_path = '/jukebox/LightSheetData/atlas/neuroglancer/atlas/princetonmouse' 
	cv_environment = {
        'PYTHONPATH':'/opt/libraries',
        'CONFIGPROXY_AUTH_TOKEN':"'31507a9ddf3e41cf86b58ffede2db68326657437704461ae2c1a4018d55e18f0'",
        'SESSION_NAME':session_name
    }
	cv1_mounts = {
		cv1_localhost_path:{
			'bind':'/mnt/data',
			'mode':'ro'
			},
	}
	cv1_container = client.containers.run('cloudv_test',
								  volumes=cv1_mounts,
								  environment=cv_environment,
								  network='nglancer',
								  name=cv1_container_name,
								  detach=True)
	return "launched cloudvolume"

@main.route("/dest",methods=['POST'])
def dest():
	logging.debug("")
	logging.debug("Here!")
	if request.method == 'POST':
		logging.debug(request.json)
		return "Got the data!"
