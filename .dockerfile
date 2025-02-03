# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV DEBUG=True

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Update the package lists and upgrade the packages
# RUN apt-get update && apt-get upgrade -y && apt-get install -y build-essential

# Install Python Installer Packages
RUN pip install --upgrade pip

# Explicitly upgrade setuptools to the desired version
RUN pip install --upgrade setuptools

# Install other Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Remove unnecessary packages to reduce image size
# RUN apt-get remove -y build-essential && apt-get autoremove -y && apt-get clean

# Copy the current directory contents into the container at /app
COPY . .

# Remove the setuptools-65.5.0.dist-info folder to fix vulnerabilies (issues CVE-2024-6345 and CVE-2022-40897)
RUN rm -rf /app/.venv/Lib/site-packages/setuptools-65.5.0.dist-info

# Expose port 5000
EXPOSE 5000

# Run the Flask app using Python
CMD ["python", "-m", "flask", "run"]
