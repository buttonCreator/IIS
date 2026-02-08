FROM python:3.9-slim

COPY send_requests.py /app/send_requests.py
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "send_requests.py"]
