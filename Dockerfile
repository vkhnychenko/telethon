FROM python:3.9-slim

RUN apt update && apt-get install -y cron rsyslog

WORKDIR /app
COPY . /app

COPY cron.d /etc/cron.d/sample

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install --no-cache-dir -r requirements.txt

CMD service rsyslog start && service cron start /var/log/syslog