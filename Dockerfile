# Use a lightweight Python image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
# Install Python dependencies and essential tools in a single RUN command
RUN apt-get update && apt-get install -y --no-install-recommends \
    vim \
    curl \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the application code into the container
COPY . /app

# Expose any necessary ports (if needed for APIs or other services)
EXPOSE 8080

# Command to run the application
CMD ["python", "main.py"]
