install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m textblob.download_corpora --quiet
	python -m pytest -vv test_*.py --cov=wikiphrases --cov=nlplogic test_corenlp.py

format:
	black *.py nlplogic

lint:
	pylint --disable=R,C,E1120 *.py

all: install lint test
