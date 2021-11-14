FROM python:3.9-slim-bullseye

RUN apt-get update && apt-get install -y tzdata && rm -rf /var/lib/apt/list/*

WORKDIR /tmp/work

COPY requirements.txt ${PWD}

RUN pip install -r requirements.txt

ENV TZ=Asia/Tokyo

ENV USER testuser1

RUN useradd -m ${USER} --uid 1000

RUN gpasswd -a ${USER} sudo

RUN "${USER}:${DOCKER_USER_PASSWORD}" | chpasswd

USER ${USER}