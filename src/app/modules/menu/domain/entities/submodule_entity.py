from datetime import datetime

class SubModuleEntity:
    
    def __init__(
        self,
        submo_Id: int,
        submo_Nombre: str,
        submo_Codigo: str,
        submo_Activo: bool,
        submo_ModuloId: int,
        submo_Creacion: datetime,
        submo_Modificacion: datetime
    ):
        self.submo_Id = submo_Id
        self.submo_Nombre = submo_Nombre
        self.submo_Codigo = submo_Codigo
        self.submo_Activo = submo_Activo
        self.submo_ModuloId = submo_ModuloId
        self.submo_Creacion = submo_Creacion
        self.submo_Modificacion = submo_Modificacion