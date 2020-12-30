FROM tensorflow/tensorflow:2.4.0

COPY ./requirements.txt /home/requirements.txt

RUN apt-get update && apt-get upgrade -y
# RUN apk update && apk upgrade

# INSTALL REQUIREMENTS FOR INSTALLING REQUIREMENTS
# RUN apk add -U --no-cache bash python3 python3-dev libpq postgresql-dev unixodbc-dev musl-dev g++ libffi-dev
# RUN pip3 install --upgrade pip
# RUN pip3 install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow_cpu-2.4.0-cp38-cp38-manylinux2010_x86_64.whl
RUN pip3 install --no-cache-dir -r /home/requirements.txt
# RUN ln -s /usr/bin/python3 /usr/bin/python
# RUN apk del --no-cache python3-dev postgresql-dev unixodbc-dev musl-dev g++ libffi-dev
