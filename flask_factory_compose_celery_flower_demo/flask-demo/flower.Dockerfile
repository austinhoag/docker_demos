FROM python:3.7-alpine

COPY celery_flower_requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD celery flower -A celery_worker.cel --address=0.0.0.0 --port=5555 --loglevel=info	