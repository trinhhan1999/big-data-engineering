# Dockerfile for custom Airflow image with additional dependencies
FROM apache/airflow:3.1.2

USER root

# Copy requirements file
COPY requirements.txt /requirements.txt

USER airflow

# Install additional Python packages
RUN pip install --no-cache-dir -r /requirements.txt
