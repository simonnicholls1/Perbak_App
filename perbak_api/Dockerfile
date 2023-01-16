FROM python:3.9-slim-buster

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create and set working directory
RUN mkdir /app
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose port for the API
EXPOSE 8000

# Run the command to start the API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
