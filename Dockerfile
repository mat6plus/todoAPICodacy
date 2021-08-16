FROM python:3

ENV PYTHONUNBUFFERED=1
WORKDIR /todoapi
COPY requirements.txt /todoapi
RUN pip install -r requirements.txt
COPY . /todoapi/