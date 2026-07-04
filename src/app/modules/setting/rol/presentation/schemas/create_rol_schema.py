from pydantic import BaseModel

class CreateRolSchema (BaseModel):
    
    rol_Nombre: str
    rol_Descripcion: str
    rol_CreacionId: int | None = None