from pydantic import BaseModel

class CreateUserSchema( BaseModel ):
    
    usua_Nombre: str
    
    usua_NombreUsuario: str
    
    usua_RolId: int
    
    usua_Contrasenia: str
    
    usua_CreacionId: int | None = None
    
    usua_ModificacionId: int | None = None
    

class LoginSchema( BaseModel ):
    
    usua_NombreUsuario: str
    
    usua_Contrasenia: str
    
class RefressTokenSchema(BaseModel):
    
    refressToken : str