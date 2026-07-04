from abc import ABC, abstractmethod
from app.modules.auth.domain.types.create_user_permission_input import CreateUserPermissionInput
from app.modules.auth.domain.entities.user_permission_entity import UserPermission

class UserPermissionRepository( ABC ):
    
    @abstractmethod
    def save(self, id_user: int, permissions: list[CreateUserPermissionInput] ) -> list[UserPermission]:
        pass
    
    @abstractmethod
    def find_all_by_id_user( self , id_user: int ) -> list[UserPermission]:
        pass