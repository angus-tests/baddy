# ==============================
# 1. Builder Stage (Python Dependencies)
# ==============================
FROM python:3.13-slim AS builder

# Set environment variables for Poetry
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.2 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PATH="/app/.venv/bin:/root/.local/bin:$PATH"

# Install system dependencies (only required for build)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry in builder
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set working directory
WORKDIR /app

# Copy only dependency files to leverage caching
COPY pyproject.toml poetry.lock ./

# Install dependencies inside the project virtual environment
RUN poetry install --no-root --no-dev

# ==============================
# 2. Frontend Builder Stage (Tailwind & Static Files)
# ==============================
FROM node:20 AS frontend-builder

# Set working directory and install Node dependencies
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install

# Copy frontend files and build Tailwind CSS
COPY . .
RUN npm run build

# ==============================
# 3. Final Stage (Runtime)
# ==============================
FROM python:3.13-slim

# Install only runtime system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 nginx \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:/root/.local/bin:$PATH" \
    DJANGO_ENV=production

# Set working directory
WORKDIR /app

# Copy Poetry from builder
COPY --from=builder /root/.local /root/.local

# Copy installed Python dependencies (Poetry virtual environment)
COPY --from=builder /app/.venv /app/.venv

# Copy application source code (only necessary files)
COPY . .

# Copy built static files from the frontend builder stage
COPY --from=frontend-builder /app/static /app/static

# Collect static files using Poetry
RUN poetry run python manage.py collectstatic --noinput

# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Create a new user and group for Nginx and adjust permissions
RUN addgroup --system nginx && adduser --system --ingroup nginx nginx && \
    chown -R nginx:nginx /app/static

# Copy and set executable the entrypoint script
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expose the port for Nginx
EXPOSE 80

# Set the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
