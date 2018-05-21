FROM rethinkdb:2.3.6

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python-pip && \
    apt-get install -y virtualenv

WORKDIR /scripts

COPY ./requirements.txt .
COPY ./prep.sh .

RUN ./prep.sh

COPY . .

RUN ./setup.sh

WORKDIR /data

EXPOSE 28015

ENTRYPOINT [ "/scripts/initialize.sh" ]
CMD ["rethinkdb", "--bind", "all"]