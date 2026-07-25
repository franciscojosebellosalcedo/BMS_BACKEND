from typing import TypedDict

class CreateUserPermissionInput ( TypedDict ):
    
    peusua_UsuarioId : int
    peusua_OpcionId : int
    peusua_Crear : bool
    peusua_Editar : bool
    peusua_CambiarEstado : bool
    peusua_CreacionId : int
    peusua_ModificacionId : int