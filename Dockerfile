FROM python:3.9

LABEL maintainer="balex89@gmail.com"

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY src .

ENV FLASK_APP=app.main

ENTRYPOINT python3 -m flask run -h 0.0.0.0 -p 5000

EXPOSE 5000
