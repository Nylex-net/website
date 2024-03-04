FROM postgres:13-alpine

COPY ./backup_file.dump /tmp/backup_file.dump

COPY ./run.sh ./scripts/run.sh

CMD ["./scripts/run.sh"]