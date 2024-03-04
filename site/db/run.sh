psql -U postgres -d django_db;
pg_restore -U postgres -d django_db /tmp/backup_file.dump;