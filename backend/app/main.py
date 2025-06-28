from fastapi import FastAPI
from app.api.v1 import endpoints

app = FastAPI(title="RizzMatch API")

app.include_router(endpoints.router)
