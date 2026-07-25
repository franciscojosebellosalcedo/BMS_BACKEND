
from app.modules.setting.rol.domain.repositories.rol_permission_repository import RolPermissionRepository
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.modules.setting.rol.infraestructure.persistence.rol_permission_model import RolPermissionModel
from app.modules.setting.rol.domain.entities.rol_permission_entity import RolPermissionEntity
from app.modules.setting.rol.domain.types.save_rol_permission_input import SaveRolPermissionInput

class RolPermissionRepositoryImpl ( RolPermissionRepository ):
    
    def __init__(self, db: Session):
        self.db = db
    
    def save(self, permissions: list[SaveRolPermissionInput] ):
        
        for perm in permissions:
            
            permission_new = RolPermissionModel(
                perol_RolId = perm["perol_RolId"],
                perol_OpcionId = perm["perol_OpcionId"],
                perol_Crear = perm["perol_Crear"],
                perol_Editar = perm["perol_Editar"],
                perol_CambiarEstado = perm["perol_CambiarEstado"],
                perol_CreacionId = perm["perol_CreacionId"],
                perol_ModificacionId = perm["perol_ModificacionId"],
            )
            
            self.db.add(permission_new)
            self.db.commit()
            self.db.refresh(permission_new)

    def find_by_id_rol(self, rol_Id: int) -> list[RolPermissionEntity]:
        
        stmt = select( RolPermissionModel ).where(
            RolPermissionModel.perol_RolId == rol_Id 
        )
        
        return self.db.execute( stmt ).scalars().all()