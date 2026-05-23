from fastapi import APIRouter
from app.core.config import settings
from app.modules.auth.presentation.routes.auth_routes import auth_routes
from app.modules.auth.presentation.routes.user_routes import  user_routes

api_routes = APIRouter(
    prefix = settings.API_PREFIX
)

api_routes.include_router( auth_routes )
api_routes.include_router( user_routes )

@api_routes.get("/")
def get_base():
    return f"Bienvenido a {settings.APP_NAME}"