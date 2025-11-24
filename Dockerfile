FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y nodejs npm && rm -rf /var/lib/apt/lists/*
COPY . .
RUN cd web/frontend && npm install && npm run build
CMD sh -c "python bot/main.py & uvicorn web.backend.main:app --host 0.0.0.0 --port 8000"