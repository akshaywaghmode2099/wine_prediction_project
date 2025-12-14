FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY app.py ./app.py
COPY model.pkl ./model.pkl
COPY Templates/ index.html
COPY Templates/ index1.html

EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
