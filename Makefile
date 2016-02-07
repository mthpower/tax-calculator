.PHONY: clean-pyc clean-build clean test

# Guess which command to use to open files.
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
	OPEN_CMD := xdg-open
endif
ifeq ($(UNAME_S),Darwin)
	OPEN_CMD := open
endif

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean: clean-build clean-pyc

dist-clean: clean

dpkg:
	if [ ! -d dist ]; then \
	    mkdir dist; \
	fi;
	if [ -e ./dist/*.deb ]; then \
	    sudo rm ./dist/*.deb; \
	fi;
	sudo docker build \
	    --file=./debian/Dockerfile \
	    --tag=tax-calculator-build \
	    .
	sudo docker run \
	    --volume=$$(pwd)/dist:/mnt/dist \
	    tax-calculator-build

env:
	virtualenv .env --clear
	./.env/bin/pip install --upgrade pip --upgrade setuptools wheel
	./.env/bin/pip install flake8 pep257 pytest pytest-django pytest-cov tox
	./.env/bin/pip install sphinx alabaster

frozen-requirements:
	virtualenv .frozenenv --clear -p $$(which pypy3)
	./.frozenenv/bin/pip install --upgrade pip --upgrade setuptools wheel
	./.frozenenv/bin/pip install .
	./.frozenenv/bin/pip freeze | grep -v ".dev" | grep -v "tax-calculator" > requirements.txt
	git add requirements.txt
	git diff --staged requirements.txt

test: env
	./.env/bin/tox
