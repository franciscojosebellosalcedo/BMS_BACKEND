
from app.modules.auth.domain.repositories.rol_repository import RolRepository
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.modules.auth.infraestructure.persistence.rol_model import RolModel
from app.modules.auth.domain.entities.rol_entity import RolEntity

class RolRepositoryImpl( RolRepository ):
    
    def __init__(self, db: Session ):
        self.db = db
    
    def find_by_id(self , id)-> RolEntity | None:
        
        stmt = select( RolModel ).where(
            RolModel.rol_Id == id
        )
        
        result = self.db.execute(stmt)
        return result.scalar_one_or_none()
    
    def create(values):
        pass
    
    def update(id, values):
        pass