# Start with a stable Python version
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements file first for caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# --- NEW STEP: Download the model during the build ---
# Copy the download script and run it. The model will be part of the image.
COPY download_model.py .
RUN python download_model.py
# --- END OF NEW STEP ---

# Copy the rest of your application files
COPY . .

# Expose the Streamlit port
EXPOSE 8501

# The command to run the application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]