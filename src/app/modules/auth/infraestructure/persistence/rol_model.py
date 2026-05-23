
from app.core.database import Base
from sqlalchemy import String, Integer, Column, Boolean, DateTime, func

class RolModel( Base ):
    
    __tablename__ = "roles"
    
    rol_Id = Column(
        Integer,
        nullable= False,
        primary_key= True
    )
    
    rol_Nombre = Column(
        String(100),
        nullable= False,
        unique= True
    )
    
    rol_Activo = Column(
        Boolean,
        nullable= False,
        default= True
    )
    
    rol_Creacion = Column(
        DateTime,
        nullable= False,
        server_default= func.now(),
    )
    
    rol_Modificacion = Column(
        DateTime,
        nullable= False,
        server_default= func.now(),
        server_onupdate= func.now()
    )
    
    rol_CreacionId = Column(
        Integer,
        nullable= False
    )
    
    rol_ModificacionId = Column(
        Integer,
        nullable= False,
        default= 0
    )