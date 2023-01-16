FROM python:3.9-slim

# Set working directory
WORKDIR $HOME

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY etl_service/ .

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Run the command to start the ETL service
CMD ["python", "etl_service/main.py"]
