SHELL := /bin/bash

PROJECT    := 'co'
LOCALPATH  := $(CURDIR)/
ENV        := $(VIRTUAL_ENV)
PYTHONPATH := $(ENV)/lib/python3.5
PYTHON_BIN := $(ENV)/bin/python3.5

BIN            := $(ENV)/bin
OPEN           := xdg-open
SYS_VIRTUALENV := virtualenv

.PRECIOUS: quit
quit:
	if [ "${$?}" = 1 ]; then exit 1; fi

.DEFAULT: install build
install:
	pip install -r requirements.txt

build:
	python -O app/main.py

.PHONY: start clean
start:
	python -d app/main.py || make quit && make clean

clean:
	rm -rf app/*.pyc
	rm -rf app/__pycache__
	rm -rf app/co/__pycache__
