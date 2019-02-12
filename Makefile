install:
	python3 -m venv .venv
	source .venv/bin/activate
	pip3 install -r requirements.txt
	deactivate

test:
	source .venv/bin/activate
	pytest
	deactivate

uninstall:
	rm -rf .venv