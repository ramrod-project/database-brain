FROM alpine:3.7

RUN apk add --update bash rethinkdb py-pip python3 && rm -rf /var/cache/apk/*

RUN pip install --upgrade virtualenv==15.1.0

VOLUME [ "/logs" ]

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