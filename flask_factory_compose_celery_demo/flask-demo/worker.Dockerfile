FROM python:3.7-alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD celery worker -A celery_worker.cel --loglevel=info	