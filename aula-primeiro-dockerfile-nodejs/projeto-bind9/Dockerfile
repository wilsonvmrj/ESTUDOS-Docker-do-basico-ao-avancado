FROM ubuntu:bionic

RUN apt-get update \
    && apt-get install -y \
    bind9 \
    bind9utils \
    bind9-doc

EXPOSE 53

RUN sed -i 's/OPTIONS=.*/OPTIONS="-4 -u bind"/' /etc/default/bind9

COPY named.conf.options /etc/bind
COPY named.conf.local /etc/bind
COPY db.minhaempresa.com.br /etc/bind/zones/


CMD [ "/bin/bash","-c", "while :; do sleep 10; done" ]