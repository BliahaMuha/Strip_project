# pull official base image
FROM python:3.9.6-alpine

# set work directory
# WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY . /code/

# install dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip

COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh
# copy project
# COPY ./entrypoint.sh.

ENTRYPOINT ["/code/entrypoint.sh"]