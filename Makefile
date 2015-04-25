ENTER_VENV := . venv/bin/activate
VENV_BIN := venv/bin/activate

init: 
	$(ENTER_VENV); pip install -r requirements/dev.txt

tests:
	$(ENTER_VENV); cd nestoria; python -m unittest discover

pylint:
	$(ENTER_VENV); pylint --rcfile=.pylintrc nestoria 

codeship.init:
	pip install -r requirements/dev.txt

codeship.tests:
	cd nestoria; python -m unittest discover

