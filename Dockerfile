FROM python:3.10-slim

WORKDIR /mcp

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "mcp.py"]