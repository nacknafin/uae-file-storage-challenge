from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api import router as api_router

app_path = Path(__file__).parent.resolve()
app = FastAPI()

app.include_router(api_router, prefix="")
app.mount("/static", StaticFiles(directory=f"{app_path}/static", html=True), name="static")
