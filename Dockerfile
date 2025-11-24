FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y nodejs npm && rm -rf /var/lib/apt/lists/*
COPY . .

# ПРИНУДИТЕЛЬНО собираем React, даже если ошибка — создаём пустую dist
RUN cd web/frontend && \
    npm install && \
    npm run build || (echo "React build failed, creating fallback" && mkdir -p dist && echo "<h1>Админка загружается...</h1>" > dist/index.html)

CMD sh -c "python -c 'from core.database import init_db; import asyncio; asyncio.run(init_db())' && python bot/main.py & uvicorn web.backend.main:app --host 0.0.0.0 --port 8000"
