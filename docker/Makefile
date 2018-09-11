dockerhubId = d8aspring
images = ${dockerhubId}/otonari_workspace

all: start


setup:
	cp .env.local .env
	cp ./images/mysql/docker-entrypoint/createdb.sql.local ./images/mysql/docker-entrypoint/createdb.sql

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
