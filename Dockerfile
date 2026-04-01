FROM python:3.12-alpine

# Upgrade zlib to ≥1.3.2-r0 to fix CVE-2026-22184
RUN apk upgrade --no-cache zlib

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
