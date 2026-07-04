
from app.modules.auth.infraestructure.repositories.user_repository_impl import UserRepositoryImpl
from app.modules.setting.rol.infraestructure.repositories.rol_repository_impl import RolRepositoryImpl
from app.modules.auth.infraestructure.repositories.user_permission_repository_impl import UserPermissionRepositoryImpl
from app.modules.auth.presentation.schemas.auth_schema import LoginSchema, RefressTokenSchema
from app.modules.auth.application.use_cases.login_case_use import LoginCaseUse
from app.modules.auth.application.use_cases.refress_session_use_case import RefressSessionUseCase
from fastapi import APIRouter, Depends
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.core.responses import success_response
from app.shared.constants.response_codes.auth_response_codes import AuthResponseCodes

auth_routes = APIRouter(
    prefix="/auth"
)

@auth_routes.post("/login")
def login(
    body: LoginSchema,
    db: Session = Depends( get_db )
):
    
    repository_user = UserRepositoryImpl( db )
    repository_rol = RolRepositoryImpl( db )
    repository_permission = UserPermissionRepositoryImpl( db )
    
    case_use = LoginCaseUse( repository_user, repository_rol, repository_permission )
    
    data = case_use.execute(body.model_dump() )
    
    return success_response( 
        code=AuthResponseCodes.AUTH_LOGIN_SUCCESS , 
        message="Credenciales validas", 
        data=data 
    )
    
@auth_routes.post("/refress")
def refress_token(
    body: RefressTokenSchema,
    db: Session = Depends(get_db)
):
    
    repositoryUser = UserRepositoryImpl( db )
    repositoryRol = RolRepositoryImpl( db )
    repository_permission = UserPermissionRepositoryImpl( db )
    
    case_use = RefressSessionUseCase(repositoryUser, repositoryRol, repository_permission )
    
    data = case_use.execute(body.refressToken)
    
    return success_response(
        code=AuthResponseCodes.AUTH_LOGIN_SUCCESS , 
        message="Credenciales validas", 
        data=data 
    )
    