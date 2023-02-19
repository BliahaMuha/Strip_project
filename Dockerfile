FROM python:3.10-alpine

# SHELL["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /code

RUN mkdir "/code/static"
RUN mkdir "/code/media"


RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip


COPY requirements.txt /code/


COPY ./entrypoint.sh .
# WORKDIR /code
COPY . /code/

# RUN useradd -rms /bin/sh master && chmod 777 /opt /run

# RUN mkdir /code/static && mkdir /code/media && chown -R master:master /code && chmod 775 /code



COPY --chown=code:code . .

# RUN chmod +x /code/entrypoint.sh
RUN pip install -r requirements.txt

ENTRYPOINT ["/code/entrypoint.sh"]