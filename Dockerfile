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

# Install system dependencies for Nginx, PostgreSQL, and Python
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    gcc libpq-dev nginx \
    && apt-get clean


# Install only runtime dependencies (minimal)
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app/pyproject.toml /app/poetry.lock /app/

# Reinstall dependencies in case of missing files
RUN poetry install --no-root --no-dev

# Copy Django application files
COPY . /app/

# Copy built static files from frontend builder stage
COPY --from=frontend-builder /app/static /app/static

# Ensure Django_env is production
ENV DJANGO_ENV=production

# Ensure static files are collected
RUN poetry run python manage.py collectstatic --noinput

# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Create a new user and group for Nginx
RUN addgroup --system nginx && adduser --system --ingroup nginx nginx

# Ensure the Nginx user has access to the static files
RUN chown -R nginx:nginx /app/static

# Ensure the entrypoint script is accessible and executable
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expose the required port for Nginx
EXPOSE 80

# Ensure entrypoint script runs
ENTRYPOINT ["/app/entrypoint.sh"]
