# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE nylex.settings
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /requirements.txt
COPY ./nylex /nylex
COPY ./scripts /scripts

# Set the working directory in the container
WORKDIR /nylex
EXPOSE 8000
# Install any needed packages specified in requirements.txt
RUN apt-get update && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    # addgroup --system app && adduser --system --group app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    # chown -R app:app /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

# Expose the port your Django app will run on

ENV PATH="/scripts:/py/bin:$PATH"

USER root

# Run the Django development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

CMD ["run.sh"]