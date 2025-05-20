FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y docker.io && \
    apt-get clean

EXPOSE 8080 50000

VOLUME /var/jenkins_home

VOLUME /var/run/docker.sock

USER jenkins