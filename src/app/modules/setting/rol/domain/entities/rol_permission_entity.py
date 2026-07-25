import datetime

class RolPermissionEntity:
    
    def __init__(
        self,
        perol_Id: int | None,
        perol_RolId: int,
        perol_OpcionId: int,
        perol_Editar: bool,
        perol_CambiarEstado: bool,
        perol_Crear: bool,
        perol_CreacionId: int,
        perol_ModificacionId: int,
        perol_Creacion: datetime,
        perol_Modificacion: datetime
    ):
        self.perol_Id = perol_Id
        self.perol_RolId = perol_RolId
        self.perol_OpcionId = perol_OpcionId
        self.perol_Editar = perol_Editar
        self.perol_CambiarEstado = perol_CambiarEstado
        self.perol_Crear = perol_Crear
        self.perol_CreacionId = perol_CreacionId
        self.perol_ModificacionId = perol_ModificacionId
        self.perol_Creacion = perol_Creacion
        self.perol_Modificacion = perol_Modificacion