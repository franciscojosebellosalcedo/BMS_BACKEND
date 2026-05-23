
from datetime import datetime

class OptionEntity:
    
    def __init__(
        self,
        opci_Id: int,
        opci_Nombre: str,
        opci_Codigo: str,
        opci_Activo: bool,
        opci_SubmoduloId: int,
        opci_Slug: str,
        opci_Creacion : datetime,
        opci_Modificacion: datetime
    ):
        self.opci_Id = opci_Id,
        self.opci_Nombre = opci_Nombre,
        self.opci_Codigo = opci_Codigo,
        self.opci_Activo = opci_Activo,
        self.opci_SubmoduloId = opci_SubmoduloId,
        self.opci_Slug = opci_Slug,
        self.opci_Creacion = opci_Creacion,
        self.opci_Modificacion = opci_Modificacion