lint:
	poetry run isort .
	poetry run black .
.PHONY: lint