FROM continuumio/anaconda3

ADD ./requirements.txt /
ADD ./requirements.dev.txt /

RUN apt update
RUN apt install -y make iputils-ping
RUN pip install --upgrade setuptools && pip install -r requirements.txt && pip install -r requirements.dev.txt
RUN mkdir -p /root/.jupyter
COPY ./.docker/jupyter_notebook_config.json /root/.jupyter/jupyter_notebook_config.json

WORKDIR /python
EXPOSE 8888
