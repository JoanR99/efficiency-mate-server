FROM python:3.10.12-slim-bookworm
LABEL maintainer="romerojoan1999@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8080

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    adduser \
        --disabled-password \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user