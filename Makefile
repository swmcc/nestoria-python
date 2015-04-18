ENTER_VENV := . venv/bin/activate
VENV_BIN := venv/bin/activate

$(VENV_BIN):
	virtualenv venv --distribute

init: 
	$(ENTER_VENV); pip install -r requirements/dev.txt

tests:
	cd nestoria; python -m unittest discover
