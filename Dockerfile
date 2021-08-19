FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /todoapicodacy

COPY requirements.txt /todoapicodacy/
RUN pip install -r requirements.txt
COPY . /todoapicodacy/

