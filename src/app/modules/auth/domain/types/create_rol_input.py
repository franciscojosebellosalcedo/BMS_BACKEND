from typing import TypedDict

class CreateRolInput( TypedDict ):
    rol_Nombre: str
    rol_CreacionId: int
    
class UpdateRolInput( TypedDict ):
    rol_Nombre: str
    rol_ModificacionId: int