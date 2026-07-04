from app.modules.setting.rol.domain.repositories.rol_repository import RolRepository
from app.shared.constants.response_codes.rol_response_codes import RolResponseCodes
from app.modules.setting.rol.domain.entities.rol_entity import RolEntity
from app.shared.exceptions.app_exception import AppException

class DisableRolCaseUse():
    
    def __init__(self, repository: RolRepository ):
        self.repository = repository
    
    def execute(self, id: int, user_id: int) -> RolEntity | None:
        
        exist = self.repository.find_by_id( id )
        
        if not exist :
            raise AppException(
                RolResponseCodes.ROL_NOT_FOUND,
                "Rol no encontrado"
            )
        
        return self.repository.disable( id, user_id )