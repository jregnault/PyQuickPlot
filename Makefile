install:
	pip3 install --upgrade pip
	pip3 install -r requirements.txt

userInstall:
	pip3 install --user --upgrade pip
	pip3 install --user -r requirements.txt

virtualenv:
	python3 -m virtualenv .pji

test:
	pip install -e pyQuickPlot
	pytest

.PHONY: install userInstall test