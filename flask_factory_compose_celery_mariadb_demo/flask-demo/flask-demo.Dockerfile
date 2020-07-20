FROM python:3.7-alpine

# Copy requirements over first so that they can be cached if they are not changed
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD python run.py