
from app.modules.auth.infraestructure.repositories.user_repository_impl import UserRepositoryImpl
from app.modules.auth.presentation.schemas.auth_schema import CreateUserRequestSchema
from app.modules.auth.application.use_cases.create_user_use_case import CreateUserUseCase
from fastapi import APIRouter, Depends
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.core.responses import success_response
from app.shared.constants.response_codes.user_response_codes import UserResponseCodes
from app.shared.guards.auth_guard import get_current_user
from app.modules.auth.infraestructure.repositories.user_permission_repository_impl import UserPermissionRepositoryImpl

user_routes = APIRouter(
    prefix="/users",
    dependencies= [
        Depends(get_current_user)
    ]
)

@user_routes.post("/register")
def register(
    body: CreateUserRequestSchema,
    db:Session = Depends( get_db ),
    current_user = Depends( get_current_user )
):
    
    repository = UserRepositoryImpl( db )
    permission_repository = UserPermissionRepositoryImpl( db )
    
    user = body.user
    
    for permission in body.permissions:

        permission.peusua_CreacionId = current_user.usua_Id
        permission.peusua_ModificacionId = current_user.usua_Id
        
    user.usua_CreacionId = current_user.usua_Id
    user.usua_ModificacionId = current_user.usua_Id
    
    case_use = CreateUserUseCase( repository, permission_repository )
    
    result = case_use.execute( body.model_dump() )
    
    return success_response(
        ok=True,
        code=UserResponseCodes.USER_CREATED,
        data=result,
        status_code=201,
        message="Usuario creado"
    )