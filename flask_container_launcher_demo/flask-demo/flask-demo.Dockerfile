FROM python:3.7.6-slim-buster

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

# Make lightservuser 
RUN useradd -r -u 153574 -d /home/lightservuser -m lightservuser
# Give read and write permissions to lightservuser /app
RUN chown -R lightservuser /app

# Set active user lightservuser
USER lightservuser

CMD python run.py