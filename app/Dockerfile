FROM python:3.8-alpine

WORKDIR /code

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code/static

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# install requirements
RUN pip install --upgrade pip \
    && pip install pipenv
COPY Pipfile /code/
RUN pipenv install --skip-lock --system

# copy project
COPY . /code
