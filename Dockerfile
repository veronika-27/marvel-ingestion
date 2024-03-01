FROM python:3.10

WORKDIR /

COPY requirements.txt requirements.txt
COPY src src

RUN pip install -r requirements.txt
