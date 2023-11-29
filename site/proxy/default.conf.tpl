server {
    listen ${LISTEN_PORT};
    server_name ${DOMAIN} ws-henry.${DOMAIN};

    location /.well-known/acme-challenge/ {
        root /vol/www/;
    }

    location /static {
        alias /vol/static;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}