from fastapi import APIRouter
from app.core.config import settings
from app.modules.auth.presentation.routes.auth_routes import auth_routes
from app.modules.auth.presentation.routes.user_routes import  user_routes
from app.modules.menu.presentation.routes.menu_router import menu_router
from app.modules.setting.rol.presentation.routes.rol_router import rol_router

api_routes = APIRouter(
    prefix = settings.API_PREFIX
)

api_routes.include_router( auth_routes )
api_routes.include_router( user_routes )
api_routes.include_router( menu_router )
api_routes.include_router( rol_router )

@api_routes.get("/")
def get_base():
    return f"Bienvenido a {settings.APP_NAME}"