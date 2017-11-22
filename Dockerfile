FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
COPY ./config /config
RUN mkdir /cliente
WORKDIR /cliente
RUN apt-get update && apt-get install -y \
python3-dev
ADD requirements/common.txt /cliente/
ADD requirements/dev.txt /cliente/
ADD . /cliente
RUN pip install -r /cliente/dev.txt