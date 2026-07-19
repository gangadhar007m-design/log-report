FROM python:3.11-slim-bookworm AS builder

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.5.2

WORKDIR /app

COPY access.log /app/access.log
