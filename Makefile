.PHONY:  build_lambda

build_lambda:
	rm -rf app/build || true
	mkdir app/build
	BUILDKIT=1 docker build app -t lambda-builder:latest -f tools/scripts/Dockerfile.lambda
	# More to dodocker run -v build:buil