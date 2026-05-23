
from typing import TypedDict, NotRequired

class UpdateUserInput(TypedDict):
    
    usua_Nombre: NotRequired[str]
    
    usua_NombreUsuario: NotRequired[str]
    
    usua_Contrasenia: NotRequired[str]
    
    usua_RolId: NotRequired[str]
    
    usua_ModificacionId: int