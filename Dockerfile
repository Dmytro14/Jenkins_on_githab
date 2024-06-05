FROM python:3.9-slim

WORKDIR /app

COPY metrics_exporter.py .

RUN pip install prometheus_client

CMD ["python", "metrics_exporter.py"]