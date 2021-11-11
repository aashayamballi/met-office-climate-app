FROM python:3.9-slim-buster

WORKDIR /weather_api_backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY req.txt .
RUN pip3 install -r req.txt

COPY . .