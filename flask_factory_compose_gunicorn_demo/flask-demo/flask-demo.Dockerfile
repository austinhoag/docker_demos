FROM python:3.7-alpine

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

# CMD python run.py
CMD gunicorn -w 3 run:app -b 0.0.0.0:5005