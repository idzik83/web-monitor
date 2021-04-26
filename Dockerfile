FROM python:3.8-buster

WORKDIR app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt  --no-dependencies

COPY web_monitor .

#CMD