FROM rethinkdb:2.3.6

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python-pip && \
    apt-get install -y virtualenv

WORKDIR /scripts

COPY . .

RUN ./initialize.sh

WORKDIR /data

CMD ["rethinkdb", "--bind", "all"]

EXPOSE 28015