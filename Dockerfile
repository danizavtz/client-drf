FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /cliente
WORKDIR /cliente
ADD requirements/common.txt /cliente/
ADD requirements/dev.txt /cliente/
RUN pip install -r requirements/dev.txt
ADD . /cliente/