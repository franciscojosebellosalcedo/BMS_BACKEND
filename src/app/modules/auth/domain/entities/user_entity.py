from datetime import datetime

class UserEntity:
    
    def __init__(
        self,
        usua_Id: int | None,
        usua_Nombre: str,
        usua_NombreUsuario: str,
        usua_Contrasenia: str,
        usua_RolId: int,
        usua_Activo: bool,
        usua_Creacion: datetime,
        usua_Modificacion: datetime,
        usua_CreacionId: int,
        usua_ModificacionId: int
    ):
        self.usua_Id = usua_Id
        self.usua_Nombre = usua_Nombre
        self.usua_NombreUsuario = usua_NombreUsuario
        self.usua_RolId = usua_RolId
        self.usua_Activo = usua_Activo
        self.usua_Creacion = usua_Creacion
        self.usua_Contrasenia = usua_Contrasenia
        self.usua_Modificacion = usua_Modificacion
        self.usua_CreacionId = usua_CreacionId
        self.usua_ModificacionId = usua_ModificacionId
        