from sqlalchemy import (
    Column, String , Integer, Boolean, DateTime, func
)

from app.core.database import Base

class UserModel(Base):
    
    __tablename__ = "usuarios"
    
    usua_Id = Column(
        Integer,
        primary_key=True,
        nullable=False,
    )
    
    usua_Nombre = Column(
        String(100),
        nullable=False,
        
    )
    
    usua_RolId = Column(
        Integer,
        nullable= False
    )
    
    usua_NombreUsuario = Column(
        String(100),
        nullable=False
    )
    
    usua_Contrasenia = Column(
        String(100),
        nullable=False
    )
    
    usua_Activo = Column(
        Boolean,
        nullable=False,
        default=True
    )
    
    usua_Creacion = Column(
        DateTime,
        nullable=False,
        server_default= func.now()
    )
    
    usua_Modificacion = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    )
    
    usua_CreacionId = Column(
        Integer,
        nullable=False
    )
    
    usua_ModificacionId = Column(
        Integer,
        nullable=False,
        default= 0
    )