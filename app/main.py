import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="DomainDecker API")

cors_env = os.getenv("CORS") 

app.add_middleware(
    CORSMiddleware,
    allow_origins=[cors_env], 
    allow_credentials=True,
    allow_methods=[cors_env],
    allow_headers=[cors_env],
)

app.include_router(router)