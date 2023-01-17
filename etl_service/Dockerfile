FROM python:3.9-slim

# Set working directory
WORKDIR .

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY etl_service /etl_service
COPY perbak_shared_library /perbak_shared_library
RUN pip install --user /perbak_shared_library
ENV PYTHONPATH "${PYTHONPATH}:/perbak_shared_library"


# Set environment variable
ENV PYTHONUNBUFFERED=1

# Run the command to start the ETL service
CMD ["python", "etl_service/main.py"]
