docker rm -f $(docker ps -a | grep "flask-demo\|flask-cvlauncher\|flask-container-launcher" | awk '{print $1}')

## cleanup network to make sure a good fresh one exists
docker network rm doubleshot

docker network create --attachable doubleshot

docker-compose build 


