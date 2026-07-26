from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from app.core.database import get_db
from app.modules.menu.infraestructure.repositories.menu_repository_impl import MenuRepositoryImpl
from app.modules.menu.application.case_use.get_menu_use_case import GetMenuUseCase
from app.modules.menu.application.case_use.get_options_use_case import GetOptionsUseCase
from app.core.responses import success_response
from app.shared.constants.response_codes.menu_response_codes import MenuResponseCodes

menu_router = APIRouter(
    prefix="/menu"
)

@menu_router.get("/")
def get_menu(
    db : Session = Depends( get_db )
):
    repository = MenuRepositoryImpl( db )
    use_case = GetMenuUseCase( repository )
    
    result = use_case.execute()
    
    return success_response( MenuResponseCodes.MENU_SUCCESS , "Menu obtenido", result )
    
@menu_router.get("/options")
def get_options(
    db: Session = Depends( get_db )
):
    repository = MenuRepositoryImpl( db )
    
    use_case = GetOptionsUseCase( repository )
    result = use_case.execute()
    
    return success_response( MenuResponseCodes.GET_OPTIONS_SUCCESS , "Opciones menu obtenido", result )