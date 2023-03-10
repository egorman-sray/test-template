FROM python:3.11-buster

COPY . /app
WORKDIR /app

RUN python -m pip install -r requirements.txt  --no-cache-dir
RUN python -m pip install my_fun_service/.