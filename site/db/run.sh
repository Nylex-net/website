#!/bin/sh

set -e

# Ensure there's a space after `if` and around the brackets
if [ -f /tmp/dump.dump ]; then
    echo "Restoring dump file into the database..."

    # Drop and recreate the database using the `postgres` administrative database
    psql -U "$POSTGRES_USER" -d django_db -c "DROP DATABASE IF EXISTS $POSTGRES_DB;"
    psql -U "$POSTGRES_USER" -d django_db -c "CREATE DATABASE $POSTGRES_DB;"

    # Restore the dump file into the newly created database
    pg_restore -U "$POSTGRES_USER" -d "$POSTGRES_DB" /tmp/dump.dump;
else
    echo "Dump file not found at /tmp/dump.dump."
fi