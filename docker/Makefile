dockerhubId = d8aspring
images = ${dockerhubId}/otonari_workspace

all: start


setup:
	cp .env.local .env
	cp mysql/docker-entrypoint-initdb.d/createdb.sql.local mysql/docker-entrypoint-initdb.d/createdb.sql

#Start local development environment
start: stop
	docker-compose up -d --remove-orphans

#Stop local development environments
stop: setup
	docker-compose stop # Stop all services

clear: stop
	docker-compose rm -f # Delete all services

# Update image for test environment
build:
	docker-compose build

# Push image for test to docker hub
push: build
	docker login -u${dockerhubId}
	docker push ${images}







# Install required packages for modules
## Move this out of this Makefile because this is part of app src's work
# app_setup: start
# 	docker-compose exec  otonari_workspace bash -c  "cd api && make"
# 	docker-compose exec  otonari_workspace bash -c  "cd api-demo && make"
# 	docker-compose exec  otonari_workspace bash -c  "cd front && make"
