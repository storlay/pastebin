FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /temp/requirements.txt

RUN pip install -U pip

RUN pip install -r /temp/requirements.txt

COPY . .