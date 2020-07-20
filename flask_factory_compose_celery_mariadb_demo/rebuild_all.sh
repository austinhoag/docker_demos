docker rm -f $(docker ps -a | grep "flask_factory_compose_celery_mariadb" | awk '{print $1}' )

docker-compose build 
