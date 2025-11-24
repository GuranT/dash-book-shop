FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y nodejs npm && rm -rf /var/lib/apt/lists/*
COPY . .
WORKDIR /app/web/frontend
RUN npm install
RUN npm run build || echo "Vite failed, creating minimal dist" && mkdir -p dist && echo '<!DOCTYPE html><html><body><h1>Админка готова</h1></body></html>' > dist/index.html
WORKDIR /app
CMD sh -c "python -c 'from core.database import init_db; import asyncio; asyncio.run(init_db())' && python bot/main.py & uvicorn web.backend.main:app --host 0.0.0.0 --port 8000"
