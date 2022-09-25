FROM python:3.10-alpine

RUN mkdir /app
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev libffi-dev linux-headers build-base
RUN apk add --update --no-cache openssl-dev musl-dev libpq postgresql-libs postgresql-dev
RUN pip install pipenv
ADD ./Pipfile /app/
ADD ./Pipfile.lock /app/
RUN pipenv install
RUN apk del .tmp
ADD . /app/

CMD ["./docker-entrypoint"]