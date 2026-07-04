from fastapi import FastAPI
from app.routes.api_routes import api_routes
from app.shared.exceptions.app_exception import AppException
from app.shared.handlers.exception_handler import exception_handler
from fastapi.middleware.cors import CORSMiddleware
from create_tables import create_tables
from app.core.config import settings

create_tables()

app = FastAPI(
    title="BMS API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.APP_CORS_ORIGIN
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)

app.add_exception_handler(
    AppException,
    exception_handler
)

app.include_router( api_routes )