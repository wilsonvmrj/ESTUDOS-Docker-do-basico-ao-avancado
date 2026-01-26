FROM node:17-alpine3.14

LABEL maintainer="mateus"

HEALTHCHECK CMD \
    curl -sf http://localhost:3000 || exit 1 

RUN mkdir /var/node \
    -s /bin/bash \
    -D nodeapp && \
    apk add curl

WORKDIR /var/node

COPY app.js .

EXPOSE 3000

ARG VERSION

ENV VERSION=${VERSION:-1.0.0}

CMD [ "node","app.js" ]
