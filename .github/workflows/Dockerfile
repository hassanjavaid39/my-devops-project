# Base Image
FROM python:3.9

# Working Directory
WORKDIR /app

# Copy Source Code
COPY . .

# Install Dependencies
RUN pip install -r requirements.txt || echo "No dependencies needed"

# Run Application
CMD ["python", "app.py"]
