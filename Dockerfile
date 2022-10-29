FROM python:3.9-slim-buster

WORKDIR /app

RUN poetry export -f requirements.txt

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["uvicorn", "api.main:app"]