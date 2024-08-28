# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY book_catalog /app/book_catalog

# Expose port 8000 to the outside world
EXPOSE 8000

# Run the application
CMD ["python", "book_catalog/test_db_connection.py"]
