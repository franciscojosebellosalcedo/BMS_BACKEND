from app.core.database import Base
from sqlalchemy import Column, String, Boolean, DateTime, func, Integer

class OptionModel( Base ):
    
    __tablename__ = "opciones"
    
    opci_Id = Column(
        Integer,
        primary_key= True,
    )
    
    opci_Nombre = Column(
        String(100),
        nullable= False
    )
    
    opci_Slug = Column(
        String(100),
        nullable= False
    )
    
    opci_Codigo = Column(
        String(100),
        nullable= False
    )
    
    opci_SubmoduloId = Column(
        Integer,
        nullable= False
    )
    
    opci_Activo = Column(
        Boolean,
        nullable= False,
        default= True
    )
    
    opci_Creacion = Column(
        DateTime,
        nullable= False,
        server_default= func.now(),
        server_onupdate= func.now()
    )
    
    opci_Modificacion = Column(
        DateTime,
        nullable= False,
        server_default= func.now(),
        server_onupdate= func.now()
    )