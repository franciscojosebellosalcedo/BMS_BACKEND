
from app.core.database import Base
from sqlalchemy import Integer, DateTime, Boolean, func, Column

class UserPermissionModel ( Base ):
    
    __tablename__ = "usuarios_permisos"
    
    peusua_Id = Column(
        Integer,
        primary_key= True,
        nullable= False
    )
    
    peusua_UsuarioId = Column(
        Integer,
        nullable= False
    )
    
    peusua_OpcionId = Column(
        Integer,
        nullable= False
    )
    
    peusua_Crear = Column(
        Boolean,
        nullable= False,
        default= False
    )
    
    peusua_Editar = Column(
        Boolean,
        nullable= False,
        default= False
    )
    
    peusua_CambiarEstado = Column(
        Boolean,
        nullable= False,
        default= False
    )
    
    peusua_Creacion = Column(
        DateTime,
        nullable= False,
        server_default= func.now()
    )
    
    peusua_Modificacion = Column(
        DateTime,
        nullable= False,
        server_default= func.now(),
        server_onupdate= func.now()
    )
    
    peusua_CreacionId = Column(
        Integer,
        nullable= False
    )
    
    peusua_ModificacionId = Column(
        Integer,
        nullable= False,
        default= 0
    )

