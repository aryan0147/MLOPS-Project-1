# Use an official Python 3.10 image from Docker Hub
FROM python:3.10-slim-buster

# Install system dependencies required by some Python packages (e.g., numpy, pandas, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libcurl4-openssl-dev \
    libxml2-dev \
    libxslt1-dev \
    && apt-get clean

# Set the working directory
WORKDIR /app

# Copy only the requirements.txt first
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the application code
COPY . /app

# Expose the port Streamlit will run on
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app1.py", "--server.port=8501", "--server.address=0.0.0.0"]
