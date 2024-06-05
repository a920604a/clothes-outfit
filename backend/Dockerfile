FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir uvicorn
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 5000

# Run Uvicorn
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "5000"]


