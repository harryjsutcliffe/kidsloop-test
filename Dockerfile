# syntax=docker/dockerfile:1

FROM ubuntu:18.04


# Install dependencies
RUN apt-get update && \
    apt-get -y install apache2

RUN apt-get install -y python3

WORKDIR /src
COPY . .
RUN output="$(python3 -m robot)" && echo $output > /var/www/html/index.html


# Configure apache
RUN echo '. /etc/apache2/envvars' > /root/run_apache.sh && \
    echo 'mkdir -p /var/run/apache2' >> /root/run_apache.sh && \
    echo 'mkdir -p /var/lock/apache2' >> /root/run_apache.sh && \ 
    echo '/usr/sbin/apache2 -D FOREGROUND' >> /root/run_apache.sh && \ 
    chmod 755 /root/run_apache.sh

EXPOSE 80


CMD /root/run_apache.sh