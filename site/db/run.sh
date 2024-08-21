#!/bin/sh

set -e

psql -U postgres -d django_db;
pg_restore -U postgres -d django_db /tmp/dump.dump;