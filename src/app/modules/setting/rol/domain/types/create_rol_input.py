from typing import TypedDict

class CreateRolInput( TypedDict ):
    rol_Nombre: str
    rol_Descripcion: str
    rol_CreacionId: int | None = None
    
class UpdateRolInput( TypedDict ):
    rol_Nombre: str
    rol_Descripcion: str
    rol_ModificacionId: int | None = None