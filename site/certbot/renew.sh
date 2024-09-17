#!/bin/sh
set -e

certbot certonly \
    --authenticator dns-desec \
    --dns-desec-credentials /opt/deSEC.ini \
    -d "$DOMAIN" \
    -m "$ACME_DEFAULT_EMAIL" \
    --agree-tos -n
    
# 0 3 1 * * certbot renew --dns-dnspython --dns-dnspython-credentials /opt/renewal-deSEC.ini --quiet
echo "0 3 * * * certbot renew --authenticator dns-desec --dns-desec-credentials /opt/renewal-deSEC.ini --quiet" > /etc/crontabs/root

# Start cron in the foreground
crond -f