FROM python:3-slim

RUN apt-get update && apt-get -y upgrade && apt install -y git

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ["python3"]
CMD ["server/app.py"]