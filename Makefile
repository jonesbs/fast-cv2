start:
	poetry run uvicorn api.main:app --reload

build:
	docker build