FROM ubuntu:22.04

WORKDIR /app

# Avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install Python and required system dependencies
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install PyTorch and dependencies
RUN pip3 install --no-cache-dir \
    torch \
    transformers==4.36.2 \
    sentencepiece \
    accelerate \
    fastapi \
    uvicorn[standard]

# Copy API service code
COPY model_service.py .

# Model will be downloaded on first use
ENV TRANSFORMERS_CACHE=/app/model_cache
ENV HF_HOME=/app/model_cache

# Expose API port
EXPOSE 8000

# Start the FastAPI service
CMD ["uvicorn", "model_service:app", "--host", "0.0.0.0", "--port", "8000"]