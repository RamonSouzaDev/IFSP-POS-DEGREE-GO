# Build Stage
FROM python:3.11-slim as builder

WORKDIR /app

# Install build dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Runtime Stage
FROM python:3.11-slim as runtime

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copy source code
COPY src ./src

# Create non-root user for security
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Expose API port
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
