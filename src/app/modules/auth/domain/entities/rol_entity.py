from datetime import datetime

class RolEntity():
    
    def __init__(
        self,
        rol_Id: int | None,
        rol_Nombre: str,
        rol_Activo: bool,
        rol_Creacion: datetime,
        rol_Modificacion: datetime,
        rol_CreacionId: int,
        rol_ModificacionId: int
    ):
        self.rol_Id = rol_Id
        self.rol_Nombre = rol_Nombre
        self.rol_Activo = rol_Activo
        self.rol_Creacion = rol_Creacion
        self.rol_Modificacion = rol_Modificacion
        self.rol_CreacionId = rol_CreacionId
        self.rol_ModificacionId = rol_ModificacionId