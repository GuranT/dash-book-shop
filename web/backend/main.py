from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/", StaticFiles(directory="../frontend/dist", html=True), name="static")

@app.post("/webhook/dash")
async def dash_webhook(payload: dict):
    try:
        from core.dash import process_dash_webhook
        await process_dash_webhook(payload)
    except:
        pass
    return {"ok": True}
