install:
	pip3 install --user --upgrade pip
	pip3 install --user -r requirements.txt

test:
	pytest

.PHONY: install test