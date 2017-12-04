FROM python:3.4.5-alpine

RUN apk update && \
    apk upgrade && \
    apk add nodejs && \
    npm install -g retire && \
    apk add ruby ruby-rdoc ruby-irb && \
    gem install bundler-audit && \
    apk add openjdk8 wget zip && \
    wget -O "/tmp/dependency-check.zip" "http://dl.bintray.com/jeremy-long/owasp/dependency-check-3.0.2-release.zip" && \
    mkdir -p /opt/dependency-check && \
    unzip -d "/opt" /tmp/dependency-check.zip && \
    rm -rf /tmp/dependency-check.zip

ENV PATH "$PATH:/opt/dependency-check/bin"

WORKDIR /opt/app
COPY 4depcheck /opt/app

COPY ./dockerfiles/run.sh /
RUN chmod +x /run.sh
ENTRYPOINT ["/bin/sh","/run.sh"]