start:
	poetry run uvicorn api.main:app --reload

build:
	docker build -t fast-cv2 .

run:
	docker run -p 8000:8000 -d fast-cv2 uvicorn api.main:app --host=0.0.0.0

logs: 
	docker container logs ${id}