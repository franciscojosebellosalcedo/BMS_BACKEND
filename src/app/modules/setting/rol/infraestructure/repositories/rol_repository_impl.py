
from app.modules.setting.rol.domain.repositories.rol_repository import RolRepository
from sqlalchemy.orm import Session
from sqlalchemy import select, update
from app.modules.setting.rol.infraestructure.persistence.rol_model import RolModel
from app.modules.setting.rol.domain.entities.rol_entity import RolEntity

class RolRepositoryImpl( RolRepository ):
    
    def __init__(self, db: Session ):
        self.db = db
        
    def paginator(self, page: int, limit: int):
        
        offset = (page - 1) * limit
        
        total = self.db.query(RolModel).count()
        
        records = (
            self.db.query(RolModel)
            .offset( offset )
            .limit( limit )
            .all()
        )
        
        return records, total
    
    def find_by_id(self , id)-> RolEntity | None:
        
        stmt = select( RolModel ).where(
            RolModel.rol_Id == id
        )
        
        result = self.db.execute(stmt)
        return result.scalar_one_or_none()
    
    def disable(self, id: int, user_id: int ):
        
        stmt = update(RolModel).where(RolModel.rol_Id == id).values(
            rol_Activo = False,
            rol_ModificacionId = user_id
        )
        self.db.execute( stmt )
        self.db.commit()
        
        return self.find_by_id( id )
    
    def enable(self, id: int, user_id: int):
        
        stmt = update(RolModel).where(RolModel.rol_Id == id).values(
            rol_Activo = True,
            rol_ModificacionId = user_id
        )
        self.db.execute( stmt )
        self.db.commit()
        
        return self.find_by_id( id )
    
    def find_by_name(self, name):
        
        stmt = select( RolModel ).where(
            RolModel.rol_Nombre == name
        )
        
        return self.db.execute(stmt).scalar_one_or_none()
    
    def create(self, values):
        
        rol_new = RolModel(
            rol_Nombre = values["rol_Nombre"],
            rol_Descripcion = values["rol_Descripcion"],
            rol_CreacionId = values["rol_CreacionId"]
        )
        
        self.db.add( rol_new )
        self.db.commit()
        self.db.refresh( rol_new )
        return rol_new
    
    def update(self, id, values):
        pass