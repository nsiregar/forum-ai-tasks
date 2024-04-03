FROM python:3.10-alpine

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk update && \
    apk add postgresql-libs && \
    apk add --virtual .build-deps gcc musl-dev postgresql-dev libffi-dev

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install -r requirements.txt
RUN apk --purge del .build-deps

COPY . .
