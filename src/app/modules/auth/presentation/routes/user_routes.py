
from app.modules.auth.infraestructure.repositories.user_repository_impl import UserRepositoryImpl
from app.modules.auth.presentation.schemas.auth_schema import CreateUserSchema
from app.modules.auth.application.use_cases.create_user_use_case import CreateUserUseCase
from fastapi import APIRouter, Depends
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.core.responses import success_response
from app.shared.constants.response_codes.user_response_codes import UserResponseCodes
from app.shared.guards.auth_guard import get_current_user

user_routes = APIRouter(
    prefix="/users",
    dependencies= [
        Depends(get_current_user)
    ]
)

@user_routes.post("/register")
def register(
    body: CreateUserSchema,
    db:Session = Depends( get_db ),
    current_user = Depends( get_current_user )
):
    body.usua_CreacionId = current_user.usua_Id
    body.usua_ModificacionId = current_user.usua_Id
    
    reposity = UserRepositoryImpl( db )
    
    case_use = CreateUserUseCase( reposity )
    
    result = case_use.execute( body.model_dump() )
    return success_response(
        ok=True,
        code=UserResponseCodes.USER_CREATED,
        data=result,
        status_code=201,
        message="Usuario creado"
    )