from app.core.database import Base
from sqlalchemy import Column, String, Integer, Boolean, DateTime, func

class SubmoduleModel( Base ):
    
    __tablename__ = "submodulos"
    
    submo_Id = Column(
        Integer,
        nullable= False,
        primary_key= True
    )
    
    submo_ModuloId= Column(
        Integer,
        nullable= False,
    )
    
    submo_Indice= Column(
        Integer,
        nullable= False,
    )
    
    submo_Nombre = Column(
        String(100),
        nullable= False
    )
    
    submo_Activo = Column(
        Boolean,
        nullable= False,
        default= True
    )
    
    submo_Codigo = Column(
        String(100),
        nullable= False,
        default= ""
    )
    
    submo_Creacion = Column(
        DateTime,
        nullable= False,
        server_default= func.now(),
        server_onupdate= func.now()
    )
    
    submo_Modificacion = Column(
        DateTime,
        nullable= False,
        server_default= func.now(),
        server_onupdate= func.now()
    )