FROM nginx:1.23.0-alpine
LABEL maintainer="ws-henry"

COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./default-ssl.conf.tpl /etc/nginx/default-ssl.conf.tpl

# Comment and uncomment the two COPY Commands to test with or without certbot container.
# COPY ./cert.pem /etc/nginx/ssl/fullchain.pem
# COPY ./key.pem /etc/nginx/ssl/privkey.pem

COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh

ENV LISTEN_PORT=80
ENV APP_HOST=nylex
ENV APP_PORT=9000

USER root

RUN apk add --no-cache openssl bash && \
    mkdir -p /vol/static && \  
    chmod 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    touch /etc/nginx/conf.d/default-ssl.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default-ssl.conf && \
    apk add --no-cache openssl bash && \
    chmod +x /run.sh

VOLUME /vol/static
VOLUME /vol/www

CMD ["/run.sh"]

# Expose the port Nginx will run on (typically 80)
# EXPOSE 8000