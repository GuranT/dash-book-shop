from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

dist_path = "../frontend/dist"
if os.path.exists(dist_path):
    app.mount("/", StaticFiles(directory=dist_path, html=True), name="static")
else:
    @app.get("/")
    async def root():
        return HTMLResponse("<h1>Админка готова</h1>")

@app.post("/webhook/dash")
async def dash_webhook(payload: dict):
    try:
        from core.dash import process_dash_webhook
        await process_dash_webhook(payload)
    except:
        pass
    return {"ok": True}
