# base image
FROM python:3.11

# Necessary, so Docker doesn't buffer the output and that you can see the output 
# of your application (e.g., Django logs) in real-time.
ENV PYTHONUNBUFFERED 1

# Make a directory in your Docker image, which you can use to store your source code
RUN mkdir /webDock

# Set the /docked directory as the working directory
WORKDIR /webDock

COPY . .

COPY requirements.txt ./requirements.txt

# Get pip to download and install requirements:
RUN pip install -r requirements.txt

# Expose ports
EXPOSE 80

# Define environment variable
ENV DJANGO_SETTINGS_MODULE=nylex.settings

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]