FROM ubuntu:18.04
RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        git \
        nano \
        curl \
        python3 \
        python3-dev \
        python3-pip \
        python3-setuptools \
        rsync \
        software-properties-common \
        sudo \
        sqlite3 \
        zip \
        unzip \
        rar \
        unrar \
        apache2-utils
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip3 --no-cache-dir install --upgrade pip
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
ENTRYPOINT bash
