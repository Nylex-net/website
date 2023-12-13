# Use an official Python runtime as a parent image
FROM python:3.12-alpine3.18
LABEL maintainer="nylex.net"

# Set environment variables
ENV PYTHONUNBUFFERED 1
# ENV DJANGO_SETTINGS_MODULE nylex.settings
ENV PYTHONDONTWRITEBYTECODE 1

# Grab copy of requirements file to install dependencies.
COPY ./requirements.txt /requirements.txt

# Copy directory of Django project.
COPY ./nylex /nylex
# VOLUME /vol/web

# Copy shell script to start application.
COPY ./scripts /scripts

# Set the working directory in the container
WORKDIR /nylex

# Expose the port your Django app will run on
# EXPOSE 8000
# Install any needed packages specified in requirements.txt,
# Create a non-root user, and set ownership to that user.
RUN apk update && apk upgrade && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    apk add --upgrade --no-cache build-base linux-headers && \
    # apt-get install -y postgresql-client libpq-dev && \
    # apt-get update && \
    /py/bin/pip install -r requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home django && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R django:django /nylex && \
    chown -R django:django /vol && \
    chmod -R 775 /vol && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

# Switch to created user to avoid running as root user.
USER django

# Run the Django development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Run the Django production server
CMD ["run.sh"]