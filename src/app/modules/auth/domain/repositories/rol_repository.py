
from abc import ABC, abstractmethod
from app.modules.auth.domain.entities.rol_entity import RolEntity
from app.modules.auth.domain.types.create_rol_input import CreateRolInput, UpdateRolInput

class RolRepository( ABC ):
    
    @abstractmethod
    def find_by_id( id: int )-> RolEntity | None:
        pass
    
    @abstractmethod
    def create( values: CreateRolInput):
        pass
    
    @abstractmethod
    def update( id: int , values: UpdateRolInput ):
        pass