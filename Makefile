install:
	pip3 install -r requirements.txt

test:
	pytest

.PHONY: install test