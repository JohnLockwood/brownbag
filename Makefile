.PHONY:  build_lambda

build_lambda:
	rm -rf build || true
	rm -rf app/build || true
	mkdir app/build
	mkdir build
	BUILDKIT=1 docker build app -t lambda-builder:latest -f tools/scripts/Dockerfile.lambda	
	docker run -v /home/johnlockwood/source/brownbag/app/build:/build lambda-builder

	mv app/build/*.zip build
	rm -rf app/build || true
