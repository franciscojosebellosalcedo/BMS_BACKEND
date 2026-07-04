
from app.modules.setting.rol.domain.repositories.rol_repository import RolRepository
from app.modules.setting.rol.domain.types.create_rol_input import CreateRolInput
from app.shared.exceptions.app_exception import AppException
from app.shared.constants.response_codes.rol_response_codes import RolResponseCodes

class CreateRolUseCase():
    
    def __init__(self, repository: RolRepository ):
        self.repository = repository
        
    def execute(self, values: CreateRolInput):
        
        exist = self.repository.find_by_name( values["rol_Nombre"] )
        
        
        if not exist:
            
            return self.repository.create(values)
        
        raise AppException(
            RolResponseCodes.ROL_EXIST,
            f"Rol de nombre {values['rol_Nombre']} ya existe"
        )