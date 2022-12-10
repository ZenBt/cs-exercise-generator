.PHONY: init build rebuild migrate 

init:
	poetry install
	poetry run python manage.py migrate