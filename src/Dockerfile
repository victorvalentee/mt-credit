FROM python:3-slim

ENV PYTHONPATH /src/server

RUN apt-get update && apt-get -y upgrade && apt install -y git

WORKDIR /src

COPY requirements.txt /src
RUN pip3 install -r requirements.txt

COPY . /src

EXPOSE 5000