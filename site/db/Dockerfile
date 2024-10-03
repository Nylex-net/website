FROM postgres:13-alpine

COPY ./dump.dump /tmp/dump.dump

COPY ./run.sh ./docker-entrypoint-initdb.d/init-script.sh

RUN chmod +x /docker-entrypoint-initdb.d/init-script.sh