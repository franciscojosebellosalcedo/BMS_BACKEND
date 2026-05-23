
from abc import ABC, abstractmethod
from app.modules.auth.domain.types.create_user_input import CreateUserInput
from app.modules.auth.domain.types.update_user_input import UpdateUserInput
from app.modules.auth.domain.entities.user_entity import UserEntity

class UserRepository( ABC ):
    
    @abstractmethod
    def create_user(self, user: CreateUserInput) -> UserEntity:
        pass
    
    @abstractmethod
    def find_by_id( id: int )-> UserEntity | None:
        pass
    
    @abstractmethod
    def update_user(self , id: int , values: UpdateUserInput)-> None:
        pass
    
    @abstractmethod
    def find_by_username(self, username: str )-> UserEntity | None:
        pass