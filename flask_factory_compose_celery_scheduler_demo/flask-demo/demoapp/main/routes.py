from flask import Blueprint
from demoapp import cel


main = Blueprint('main',__name__)

@main.route("/") 
def base(): 
	return "home"

@cel.task
def my_background_task():
    # some long running task here
    return "test task complete"

@main.route("/test_celery")
def test_celery():
	task = my_background_task.delay()
	result = task.get()
	print(result)
	print(type(result))
	return "Test complete!"

