from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="DomainDecker API")

app.include_router(router)
