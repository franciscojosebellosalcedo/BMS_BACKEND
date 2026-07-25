
from app.core.database import Base
from sqlalchemy import Integer, Boolean, DateTime, func, Column

class RolPermissionModel ( Base ):
    
    __tablename__ = "rol_permisos"
    
    perol_Id = Column(
        Integer,
        primary_key= True,
        nullable= False
    )
    
    perol_RolId = Column(
        Integer,
        nullable= False
    )
    
    perol_OpcionId = Column(
        Integer,
        nullable= False
    )
    
    perol_Crear = Column(
        Boolean,
        nullable= False
    )
    
    perol_Editar = Column(
        Boolean,
        nullable= False,
    )
    
    perol_CambiarEstado = Column(
        Boolean,
        nullable= False
    )
    
    perol_CreacionId = Column(
        Integer,
        nullable= False
    )
    
    perol_ModificacionId = Column(
        Integer,
        nullable= False,
        default= 0
    )
    
    perol_Creacion = Column(
        DateTime,
        nullable= False,
        server_default= func.now()
    )
    
    perol_Modificacion = Column(
        DateTime,
        nullable= True,
        server_default= func.now(),
        server_onupdate= func.now()
    )