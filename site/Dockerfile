# Use an official Python runtime as a parent image
FROM python:3.12

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE nylex.settings
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /requirements.txt
COPY ./nylex /nylex
COPY ./scripts /scripts

# Set the working directory in the container
WORKDIR /nylex
# EXPOSE 8000
# Install any needed packages specified in requirements.txt
RUN apt-get update && \
    # apk add --upgrade --no-cache build-base linux-headers && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    useradd -ms /bin/bash django && \
    chown -R django:django /nylex && \
    chown -R django:django /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

# Expose the port your Django app will run on

ENV PATH="/scripts:/py/bin:$PATH"

USER django

# Run the Django development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Run the Django production server
CMD ["run.sh"]