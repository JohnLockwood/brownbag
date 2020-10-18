.PHONY: build run

env := development
app := api
# Doesn't work yet:
# password := $( shell aws ssm get-parameter --name /api/development/db/password --with-decryption | jq -r ".Parameter.Value" )

run: build
	echo Running...
	echo Using environment $(env)
# Doesen't work yet: echo Unsecurely printing password: $(password)

build:
	echo Building...
