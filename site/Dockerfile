# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE nylex.settings

COPY ./requirements.txt /requirements.txt
COPY ./nylex /nylex
COPY ./scripts /scripts

# Set the working directory in the container
WORKDIR /nylex
EXPOSE 80
# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home nylex && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media
    # chown -R nylex:nylex /vol && \
    # chmod -R 755 /vol

# Expose the port your Django app will run on

ENV PATH="/scripts:/py/bin:$PATH"

USER nylex

# Run the Django development server
CMD ["run.sh"]