.PHONY: build run

env := development
app := api
# Doesn't work yet:
POSTGRES_PASSWORD := $(shell aws ssm get-parameter --name /api/development/db/password --with-decryption | jq -r ".Parameter.Value")

run: build
	@ # echo Running...
	echo Using environment $(env)	
	echo Unsecurely printing password: $(POSTGRES_PASSWORD) 
	export POSTGRES_PASSWORD
	docker-compose -f api/docker-compose.yml up

build:
	@# echo Building...
