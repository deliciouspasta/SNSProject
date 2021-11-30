FROM python:3.9-slim-bullseye

RUN apt-get update && apt-get install -y tzdata && rm -rf /var/lib/apt/list/*

RUN pip install wheel

RUN apt-get install build-essential python -y

RUN apt-get install python3.9-dev -y

RUN apt-get install libpcre3-dev -y

RUN pip install uwsgi -I --no-cache-dir

RUN pip install uwsgi

WORKDIR /tmp/work

COPY requirements.txt ${PWD}

RUN pip install -r requirements.txt

ENV TZ=Asia/Tokyo

ENV USER testuser1

RUN useradd -m ${USER} --uid 1000

RUN gpasswd -a ${USER} sudo

RUN "${USER}:${DOCKER_USER_PASSWORD}" | chpasswd

USER ${USER}