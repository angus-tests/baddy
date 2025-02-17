# ==============================
# 1. Build Stage (Dependencies)
# ==============================
FROM python:3.13-slim AS builder

# Set environment variables for Poetry
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.2 \
    PATH="/root/.local/bin:$PATH"

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Copy only dependency files to leverage caching
COPY pyproject.toml poetry.lock /app/

# Install dependencies without virtual environment
RUN poetry install --no-root

# ==============================
# 2. Build Stage (Tailwind & Static Files)
# ==============================
FROM node:20 AS frontend-builder

# Set working directory
WORKDIR /app

# Copy only package.json and package-lock.json for better caching
COPY package.json package-lock.json /app/

# Install Tailwind & frontend dependencies
RUN npm install

# Copy the rest of the project (only frontend files for now)
COPY . /app/

# Build Tailwind CSS
RUN npm run build

# ==============================
# 3. Final Stage (Runtime)
# ==============================
FROM python:3.13-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PATH="/root/.local/bin:$PATH"

# Set working directory
WORKDIR /app

# Install only runtime dependencies (minimal)
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app/pyproject.toml /app/poetry.lock /app/

# Copy over scripts
COPY scripts /scripts

# Make scripts executable
RUN chmod +x /scripts/*

# Reinstall dependencies in case of missing files
RUN poetry install --no-root --no-dev

# Copy Django application files
COPY . /app/

# Install system dependencies (minimal)
RUN apt-get update && apt-get install -y libpq-dev && rm -rf /var/lib/apt/lists/*

# Copy built static files from frontend builder stage
COPY --from=frontend-builder /app/static /app/static

# Ensure static files are collected
RUN poetry run python manage.py collectstatic --noinput

# Expose the application port
EXPOSE 8000

# Run the start.sh script
ENTRYPOINT ["/scripts/start.sh"]
