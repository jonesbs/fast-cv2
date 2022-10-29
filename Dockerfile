FROM python:3.9-slim-buster

WORKDIR /app
COPY . .

RUN apt update
RUN apt install ffmpeg libsm6 libxext6  -y

RUN pip install poetry
RUN poetry export -f requirements.txt --output requirements.txt  
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["uvicorn", "api.main:app", "--host=0.0.0.0", "--port=8000"]