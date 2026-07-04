from app.core.database import Base
from sqlalchemy import Column, String, Integer, DateTime, Boolean , func

class ModuleModel( Base ):
    
    __tablename__ = "modulos"
    
    modulo_Id = Column(
        Integer,
        primary_key= True
    )
    
    modulo_Indice = Column(
        Integer,
        nullable= False
    )
    
    modulo_Nombre = Column(
        String(100),
        nullable= False
    )
    
    modulo_Codigo = Column(
        String(100),
        nullable= False,
        default= ""
    )
    
    modulo_Activo = Column(
        Boolean,
        nullable= False,
        default= True
    )
    
    modulo_Creacion = Column(
        DateTime,
        nullable= False,
        server_default= func.now(),
        server_onupdate= func.now()
    )
    
    modulo_Modificacion = Column(
        DateTime,
        nullable= False,
        server_default= func.now(),
        server_onupdate= func.now()
    )