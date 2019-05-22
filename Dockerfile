FROM python:3.6.8-stretch

ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD ./sample /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install --trusted-host pypi.python.org -r dev_requirements.txt
RUN apt-get update
RUN apt-get install -y postgresql-client
