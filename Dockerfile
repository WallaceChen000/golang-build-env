FROM phusion/baseimage:focal-1.1.0

MAINTAINER Wallace.Chen

ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
ENV DEBIAN_FRONTEND noninteractive

EXPOSE 2224

# Install basic system
RUN apt-get update && apt-get install -y software-properties-common
RUN apt-get install -qq -y \
    sudo \
    cron \
    wget \
    curl \
    vim \
    ncdu \
    python3-pip \
    iproute2

RUN apt-get install -qq -y gcc ca-certificates git less file xz-utils unzip
RUN apt-get install -qq -y protobuf-compiler   #for protoc
#RUN rm -f /bin/sh && ln -s /bin/bash /bin/sh


# ssh enable
RUN dpkg-reconfigure openssh-server && echo 'root:SystemControl' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/#Port 22/Port 2224/' /etc/ssh/sshd_config && \
    rm -f /etc/service/sshd/down

ENV ARCH=amd64
ENV GOLANG_ARCH_amd64=amd64 GOLANG_ARCH_arm=armv6l GOLANG_ARCH_arm64=arm64 GOLANG_ARCH=GOLANG_ARCH_${ARCH} \
    GOPATH=/go GOROOT=/usr/local/go GO111MODULE=auto PATH=/go/bin:/usr/local/go/bin:${PATH} SHELL=/bin/bash

#RUN wget -O - https://storage.googleapis.com/golang/go1.16.4.linux-${!GOLANG_ARCH}.tar.gz | tar -xzf - -C /usr/local
RUN wget -O - https://storage.googleapis.com/golang/go1.17.4.linux-amd64.tar.gz | tar -xzf - -C /usr/local

RUN if [ "${ARCH}" == "amd64" ]; then \
    curl -sL https://install.goreleaser.com/github.com/golangci/golangci-lint.sh | sh -s v1.39.0; \
    fi

WORKDIR /root

# Set cron job


RUN mkdir -p /etc/service/runservice/ && \
    printf '#!/bin/sh\nset -e\n\nexec /usr/local/bin/runservice.sh\n' > /etc/service/runservice/run && \
    chmod a+x /etc/service/runservice/run

# Install rootfs
COPY ./rootfs.tar.gz /root/
RUN tar -xvf /root/rootfs.tar.gz -C / && rm -f /root/rootfs.tar.gz

# Install pip package
RUN pip install -U protobuf==4.21.7 grpcio==1.47.0 grpcio-tools==1.47.0

# Install yarn & nodejs
RUN curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - && echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list && apt-get update; apt-get install yarn -qq -y

# update nodejs from 10.19.0 to v14.20.1
RUN apt purge nodejs -y && curl -sL https://deb.nodesource.com/setup_14.x | bash - && apt install nodejs -y -qq

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
