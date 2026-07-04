from pydantic import BaseModel
from app.modules.auth.presentation.schemas.user_permission_schema import UserPermissionSchema
class CreateUserSchema( BaseModel ):
    
    usua_Nombre: str
    
    usua_NombreUsuario: str
    
    usua_RolId: int
    
    usua_Contrasenia: str
    
    usua_CreacionId: int | None = None
    
    usua_ModificacionId: int | None = None

class CreateUserRequestSchema( BaseModel ):
    user: CreateUserSchema
    permissions: list[UserPermissionSchema]

class LoginSchema( BaseModel ):
    
    usua_NombreUsuario: str
    
    usua_Contrasenia: str
    
class RefressTokenSchema(BaseModel):
    
    refressToken : str