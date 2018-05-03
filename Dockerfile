FROM rethinkdb:2.3.6

RUN apt-get update && \
    apt-get install python3 && \
    apt-get install python-pip

COPY ./requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

CMD ["rethinkdb", "--bind", "all"]

EXPOSE 28015