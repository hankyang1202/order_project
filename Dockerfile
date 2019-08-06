FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update -y && apt-get -y install python3-dev
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/
