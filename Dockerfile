FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -U pip

COPY requirements.txt /temp/requirements.txt

RUN pip install -r /temp/requirements.txt

COPY . .