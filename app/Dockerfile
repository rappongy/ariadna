FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code
WORKDIR /code

RUN pip install --upgrade pip
RUN pip install pipenv          # combine with prev
COPY Pipfile /code/
RUN pipenv install --skip-lock --system --dev       # this is for dev only

COPY . /code
