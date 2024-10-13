
FROM python:latest
# Avoid writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Set the working directory
WORKDIR /scrum
# Copy the requirements file and install dependencies
COPY requirements.txt /scrum/
# Install pip, setuptools, and wheel to avoid missing package errors
RUN pip install --upgrade pip setuptools wheel
# Install the dependencies from requirements.txt
RUN pip install -r requirements.txt
# Copy the rest of the application code
COPY . /scrum/