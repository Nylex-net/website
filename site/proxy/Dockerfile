FROM nginx:1.25.3-alpine
LABEL maintainer="henatic"

# Copy current directory and store in volume directory.
COPY . /etc/nginx/

# Comment and uncomment the two COPY Commands below to test with or without certbot container.
# COPY ./cert.pem /etc/letsencrypt/live/${DOMAIN}/fullchain.pem
# COPY ./key.pem /etc/letsencrypt/live/${DOMAIN}/privkey.pem

# Copy and store other parameters.
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh

# Environmental variables.
ENV LISTEN_PORT=80
ENV APP_HOST=nylex
ENV APP_PORT=9000

# Set proxy user.
USER root

# Commands to update, create directories, and set permissions.
RUN apk update && apk upgrade && \
    apk add --no-cache openssl bash && \
    mkdir -p /vol/static && \  
    chmod 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    touch /etc/nginx/conf.d/default-ssl.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default-ssl.conf && \
    chmod +x /run.sh

# Set directories in volumes.
VOLUME /vol/static
VOLUME /vol/media
VOLUME /vol/www

# Run shell script for production.
CMD ["/run.sh"]

# Expose the port Nginx will run on (typically 80)
# EXPOSE 8000