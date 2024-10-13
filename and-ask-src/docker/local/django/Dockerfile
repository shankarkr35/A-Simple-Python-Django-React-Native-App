
FROM python:latest
# Avoid writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Set the working directory
WORKDIR /and_ask_app
# Copy the requirements file and install dependencies
COPY requirements.txt /and_ask_app/
# Install pip, setuptools, and wheel to avoid missing package errors
RUN pip install --upgrade pip setuptools wheel
# Install the dependencies from requirements.txt
RUN pip install -r requirements.txt
# Copy the rest of the application code
COPY . /and_ask_app/

