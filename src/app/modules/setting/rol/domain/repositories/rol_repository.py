
from abc import ABC, abstractmethod
from app.modules.setting.rol.domain.entities.rol_entity import RolEntity
from app.modules.setting.rol.domain.types.create_rol_input import CreateRolInput, UpdateRolInput

class RolRepository( ABC ):
    
    @abstractmethod
    def find_by_id( id: int )-> RolEntity | None:
        pass
    
    @abstractmethod
    def find_by_name( name: str )-> RolEntity | None:
        pass
    
    @abstractmethod
    def disable( id: int, user_id: int) -> RolEntity | None:
        pass
    
    @abstractmethod
    def enable( id: int, user_id: int ) -> RolEntity | None:
        pass
    
    @abstractmethod
    def paginator(page: int, limit: int ):
        pass
    
    @abstractmethod
    def create( values: CreateRolInput)-> RolEntity:
        pass
    
    @abstractmethod
    def update( id: int , values: UpdateRolInput ):
        pass