# Use Python 3.9 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the rest of the application
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Expose port 3000
EXPOSE 3000

# Command to run the application
CMD ["python", "app.py", "--host", "0.0.0.0"]