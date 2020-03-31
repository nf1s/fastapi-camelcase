test:
	pipenv run pytest

test-coverage:
	pipenv run coverage run -m pytest
	pipenv run coverage report

deploy:
	pipenv run python setup.py sdist
	pipenv run twine upload dist/*

install:
	pipenv install

deploy-docs:
	mkdocs gh-deploy

serve-docs:
	mkdocs serve