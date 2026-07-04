from sqlalchemy.orm import Session
from app.modules.auth.domain.entities.user_permission_entity import UserPermission
from app.modules.auth.infraestructure.persistence.user_permission_model import UserPermissionModel
from app.modules.auth.domain.repositories.user_permission_repository import UserPermissionRepository
from app.modules.auth.domain.types.create_user_permission_input import CreateUserPermissionInput
from  sqlalchemy import select

class UserPermissionRepositoryImpl ( UserPermissionRepository ):
    
    def __init__(self, db: Session ):
        self.db = db
        
    def find_all_by_id_user(self, id_user) -> list[UserPermission] :
        
        stmt = select( UserPermissionModel ).where( UserPermissionModel.peusua_UsuarioId == id_user )
        return self.db.execute(stmt ).scalars().all()
        
    def save(self, id_user: int, permissions: list[CreateUserPermissionInput] ) -> list[UserPermission]:
        
        for permission in permissions:
            
            permission_new = UserPermissionModel(
                **permission
            )
            
            self.db.add( permission_new )
            self.db.commit()
        
        stmt = select( UserPermissionModel ).where( UserPermissionModel.peusua_UsuarioId == id_user )
        user_permissions = self.db.execute( stmt ).scalars().all()
        
        return user_permissions
        