from pydantic import BaseModel
from app.modules.setting.rol.presentation.schemas.save_rol_permission_schema import SaveRolPermissionSchema

class RolSchema (BaseModel):
    
    rol_Nombre: str
    rol_Descripcion: str
    rol_CreacionId: int | None = None
    
class CreateRolSchema( BaseModel ):
    rol: RolSchema
    permissions: list[SaveRolPermissionSchema]