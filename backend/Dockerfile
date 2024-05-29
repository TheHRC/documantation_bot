# Use Python 3.9 image
FROM python:3.9

# Set working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Flask files into the container
COPY . .

# Expose port 5000
EXPOSE 5000

# Command to run Flask server
CMD ["python", "apis.py"]
