FROM python:3.9-slim

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Run the etl script
CMD ["python", "main.py"]
