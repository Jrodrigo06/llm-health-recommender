
FROM python:3.13.2-slim AS builder

# Sets ENV Stuff
ENV VENV_PATH=/opt/venv
RUN python -m venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      build-essential libgomp1 && \
    rm -rf /var/lib/apt/lists/*

# Installs dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . .

FROM python:3.13.2-slim

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
COPY --from=builder /app /app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

