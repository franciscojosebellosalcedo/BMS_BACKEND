from typing import TypedDict
from app.modules.auth.domain.types.create_user_permission_input import CreateUserPermissionInput

class CreateUserInput( TypedDict ):
    
    usua_Nombre: str
    
    usua_NombreUsuario: str
    
    usua_Contrasenia: str
    
    usua_RolId: str
    
    usua_CreacionId: int
    
    usua_ModificacionId: int
    
class CreateUserRequestInput( TypedDict ):
    
    user: CreateUserInput
    permissions: list[CreateUserPermissionInput]