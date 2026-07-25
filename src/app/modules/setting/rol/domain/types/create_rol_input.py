from typing import TypedDict
from app.modules.setting.rol.domain.types.save_rol_permission_input import SaveRolPermissionInput

class RolInput( TypedDict ):
    rol_Nombre: str
    rol_Descripcion: str
    rol_CreacionId: int | None = None
    
class CreateRolInput( TypedDict ):
    rol: RolInput
    permissions: list[SaveRolPermissionInput]
class UpdateRolInput( TypedDict ):
    rol_Nombre: str
    rol_Descripcion: str
    rol_ModificacionId: int | None = None