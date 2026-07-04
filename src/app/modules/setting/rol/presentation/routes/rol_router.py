from fastapi import APIRouter, Depends, Query
from app.modules.setting.rol.application.use_cases.create_rol_use_case import CreateRolUseCase
from app.modules.setting.rol.application.use_cases.paginate_rol_use_case import PaginatorUseCase
from app.modules.setting.rol.application.use_cases.disable_rol_use_case import DisableRolCaseUse
from app.modules.setting.rol.infraestructure.repositories.rol_repository_impl import RolRepositoryImpl
from app.shared.guards.auth_guard import get_current_user
from app.shared.constants.response_codes.rol_response_codes import RolResponseCodes
from app.core.responses import success_response
from app.modules.setting.rol.presentation.schemas.create_rol_schema import CreateRolSchema
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.modules.auth.domain.entities.user_entity import UserEntity

rol_router = APIRouter(
    prefix="/rols",
    dependencies=[
        Depends( get_current_user )
    ]
)

@rol_router.post("/")
def create(
    body: CreateRolSchema,
    db : Session = Depends( get_db ),
    current_user: UserEntity = Depends( get_current_user )
):
    body.rol_CreacionId = current_user.usua_Id
    
    repository = RolRepositoryImpl( db )
    use_case = CreateRolUseCase( repository )
    rol_created = use_case.execute(body.model_dump() )
    
    return success_response( RolResponseCodes.ROL_CREATED , "Rol creado correctamente", rol_created )

@rol_router.post("/paginate")
def paginator (
    db: Session = Depends( get_db ),
    page: int = Query(1 , ge = 1),
    limit: int = Query( 10, ge= 10)
):
    
    repository = RolRepositoryImpl( db )
    use_case = PaginatorUseCase( repository )
    
    data = use_case.execute( page , limit )
    
    return success_response( RolResponseCodes.ROL_PAGINATE_SUCCESS, "Paginado", data )

@rol_router.put("/disable/{id}")
def disable(
    id: int,
    db: Session = Depends( get_db ),
    current_user: UserEntity = Depends( get_current_user )
):
    repository = RolRepositoryImpl( db )
    use_case = DisableRolCaseUse( repository )
    
    result = use_case.execute( id , current_user.usua_Id )
    
    return success_response( RolResponseCodes.ROL_DISABLE_SUCCESS, "Rol deshabilitado", result)