FROM postgres:13-alpine

COPY ./dump.dump /tmp/dump.dump

COPY ./run.sh ./scripts/run.sh

CMD ["./scripts/run.sh"]