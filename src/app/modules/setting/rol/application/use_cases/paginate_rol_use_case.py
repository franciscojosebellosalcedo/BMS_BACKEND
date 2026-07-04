from app.modules.setting.rol.domain.repositories.rol_repository import RolRepository
from fastapi.encoders import jsonable_encoder
import math

class PaginatorUseCase ():
    
    def __init__(self, repository: RolRepository ):
        self.repository = repository
        
    def execute( self, page: int, limit: int ):
        
        records , total = self.repository.paginator( page, limit )
        
        data_response = {
            "records": jsonable_encoder(records ),
            "totalRecords": total, 
            "page": page,
            "limit": limit,
            "totalPages": math.ceil( total / limit )
        }
        
        return data_response