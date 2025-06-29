FROM python:3.12.3-slim

WORKDIR /app

# Install OS-level dependencies for building some Python packages
RUN apt-get update && \
    apt-get install -y \
        libsdl2-dev \
        libsdl2-mixer-dev \
        gcc \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy dependencies file and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and assets
COPY src/main.py .
COPY assets/ ./assets/

# Run the game
CMD ["python", "main.py"]

