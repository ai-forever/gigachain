FROM docker.io/library/ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive


# docker build -t demo -f ./docker/Dockerfile .
# docker run --rm -it -v $PWD:/develop -p 8888:8888 demo bash
# python3 -m jupyterlab --allow-root --ip 0.0.0.0 --port 8888

RUN apt-get update --upgrade
RUN apt-get install -y python3 python3-pip python3-venv
RUN apt-get install -y ffmpeg curl
RUN apt-get install -y wkhtmltopdf

COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /develop
