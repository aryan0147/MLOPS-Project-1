# # Use an official Python 3.10 image from Docker Hub
# FROM python:3.10-slim-buster

# # Set the working directory
# WORKDIR /app

# # Copy your application code
# COPY . /app

# # Install the dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Expose the port Streamlit will run on
# EXPOSE 8501

# # Command to run the Streamlit app
# CMD ["streamlit", "run", "app1.py", "--server.port=8501", "--server.address=0.0.0.0"]
