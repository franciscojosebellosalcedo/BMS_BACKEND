from datetime import datetime

class UserPermission:
    
    def __init__(
        self,
        peusua_Id: int | None,
        peusua_UsuarioId: int,
        peusua_OpcionId: int,
        peusua_Crear: bool,
        peusua_Editar: bool,
        peusua_CambiarEstado: bool,
        peusua_Creacion: datetime,
        peusua_Modificacion: datetime,
        peusua_CreacionId: int,
        peusua_ModificacionId: int
    ):
        self.peusua_Id = peusua_Id
        self.peusua_UsuarioId = peusua_UsuarioId
        self.peusua_OpcionId = peusua_OpcionId
        self.peusua_Crear = peusua_Crear
        self.peusua_Editar = peusua_Editar
        self.peusua_CambiarEstado = peusua_CambiarEstado
        self.peusua_Creacion = peusua_Creacion
        self.peusua_Modificacion = peusua_Modificacion
        self.peusua_CreacionId = peusua_CreacionId
        self.peusua_ModificacionId = peusua_ModificacionId