FROM python:alpine

COPY ./requirements.txt /home/requirements.txt

RUN apk update && apk upgrade

# INSTALL REQUIREMENTS FOR INSTALLING REQUIREMENTS
RUN apk add -U --no-cache bash python3 python3-dev libpq postgresql-dev unixodbc-dev musl-dev g++ libffi-dev
RUN pip3 install --no-cache-dir -r /home/requirements.txt
RUN ln -s /usr/bin/python3 /usr/bin/python
# RUN apk del --no-cache python3-dev postgresql-dev unixodbc-dev musl-dev g++ libffi-dev
