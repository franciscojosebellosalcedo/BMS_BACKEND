from pydantic import BaseModel

class UserPermissionSchema( BaseModel ):
    peusua_UsuarioId : int | None = None
    peusua_OpcionId : int
    peusua_Crear : bool
    peusua_Editar : bool
    peusua_CambiarEstado : bool
    peusua_CreacionId : int | None = None
    peusua_ModificacionId : int | None = None