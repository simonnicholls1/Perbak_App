FROM python:3.9-slim-buster

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set working directory
WORKDIR .

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY perbak_api /perbak_api
COPY perbak_shared_library /perbak_shared_library
RUN pip install --user /perbak_shared_library
ENV PYTHONPATH "${PYTHONPATH}:/perbak_shared_library"


# Expose port for the API
EXPOSE 8000

# Run the command to start the API
CMD ["uvicorn", "perbak_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
