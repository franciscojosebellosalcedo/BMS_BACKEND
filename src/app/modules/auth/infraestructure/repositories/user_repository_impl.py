from app.modules.auth.domain.repositories.user_repository import UserRepository
from sqlalchemy.orm import Session
from app.modules.auth.domain.entities.user_entity import UserEntity
from app.modules.auth.infraestructure.persistence.user_model import UserModel
from sqlalchemy import select

class UserRepositoryImpl(UserRepository):
    
    def __init__(self, db: Session):
        self.db = db
        
    def find_by_id(self, id)-> UserEntity | None:
        
        stmt = select( UserModel ).where(
            UserModel.usua_Id == id
        )
        
        result = self.db.execute( stmt )
        return result.scalar_one_or_none()
        
    def create_user(self, user):
    
        new_user = UserModel(**user)
        
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        
        return UserEntity(
            usua_Id= new_user.usua_Id,
            usua_Nombre= new_user.usua_Nombre,
            usua_NombreUsuario= new_user.usua_NombreUsuario,
            usua_RolId= new_user.usua_RolId,
            usua_Contrasenia= new_user.usua_Contrasenia,
            usua_Activo= new_user.usua_Activo,
            usua_Creacion= new_user.usua_Creacion,
            usua_Modificacion= new_user.usua_Modificacion,
            usua_CreacionId= new_user.usua_CreacionId,
            usua_ModificacionId= new_user.usua_ModificacionId
        )
        
    def update_user(self, id, values):
        pass
    
    def find_by_username(self, username: str ):
        
        stmt = select(UserModel).where(
            UserModel.usua_NombreUsuario == username
        )
        
        result = self.db.execute(stmt)
        
        return result.scalar_one_or_none()