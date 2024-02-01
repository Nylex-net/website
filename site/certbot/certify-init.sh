#!/bin/sh

# Waits for proxy to be available, then gets the first certificate.

set -e

# Use netcat (nc) to check port 80, and keep checking every 5 seconds
# until it is available. This is so nginx has time to start before
# certbot runs.

until nc -z proxy 80; do
    echo "Waiting for proxy..."
    sleep 5s & wait ${!}
done

echo "Getting certificate..."

# certbot certonly \
#     --webroot \
#     --webroot-path "/vol/www/" \
#     -d "$DOMAIN" \
#     --email $EMAIL \
#     --rsa-key-size 4096 \
#     --agree-tos \
#     --noninteractive

# certbot certonly \
#   --webroot \
#   --webroot-path "/vol/www/" \
#   --dns-dnspython \
#   --dns-dnspython-credentials /deSEC.ini \
#   -d $DOMAIN \
#   --email $EMAIL \
#   --rsa-key-size 4096 \
#   --agree-tos \
#   --noninteractive

certbot certonly \
    --authenticator dns-desec \
    --dns-desec-credentials /opt/deSEC.ini \
    -d "$DOMAIN" \
    -m "$ACME_DEFAULT_EMAIL" \
    --agree-tos -n