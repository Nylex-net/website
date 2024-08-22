FROM certbot/certbot:latest

# Commands to update, create directories, and set permissions.
COPY ./ /opt
RUN apk update && apk upgrade && \
    /usr/local/bin/python -m pip install --upgrade pip && \
    /usr/local/bin/python -m pip install certbot-dns-desec && \
    chmod +x /opt/certify-init.sh && \
    chmod +x /opt/renew.sh && \
    chmod 600 /opt/deSEC.ini && \
    chmod 600 /opt/renewal-deSEC.ini
    # chmod +x /opt/acme-dns-auth.py

# Comment/Uncomment for renewal of .pem files.
ENTRYPOINT [ ]
CMD ["/opt/renew.sh"]

# Comment/Uncomment for creation of .pem files.
# CMD ["/opt/certify-init.sh"]