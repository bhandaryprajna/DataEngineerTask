# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the files from current directory  into the container at /app
COPY  ./DataEngineerHomework.py /app
COPY  ./test_DataEngineerHomework.py /app

# Install any needed dependencies
RUN pip install --no-cache-dir pandas
RUN pip install pytest

# Run the Python script when the container launches
CMD ["pytest", "/app"]
