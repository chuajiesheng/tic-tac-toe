.DEFAULT_GOAL: all

all:	init test

init:
	virtualenv -p python3 venv && \
	source ./venv/bin/activate && \
	pip install -r requirements.txt;
	
test:
	py.test tests

