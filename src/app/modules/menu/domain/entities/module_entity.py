from datetime import datetime

class ModuleEntity():
    
    def __init__(
        self,
        modulo_Id: int,
        modulo_Nombre: str,
        modulo_Codigo: str,
        modulo_Activo: bool,
        modulo_Creacion: datetime,
        modulo_Modificacion: datetime
    ):
        self.modulo_Id = modulo_Id
        self.modulo_Nombre = modulo_Nombre
        self.modulo_Codigo = modulo_Codigo
        self.modulo_Activo = modulo_Activo
        self.modulo_Creacion = modulo_Creacion
        self.modulo_Modificacion = modulo_Modificacion
        