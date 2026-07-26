from app.modules.setting.rol.domain.repositories.rol_repository import RolRepository
from app.modules.setting.rol.domain.repositories.rol_permission_repository import RolPermissionRepository

class GetRolByIdUseCase :
    
    def __init__(self, repository_rol: RolRepository, repository_permission : RolPermissionRepository):
        self.repository_rol = repository_rol
        self.repository_permission = repository_permission
        
    def execute( self , rol_id: int):
        
        rol = self.repository_rol.find_by_id( rol_id )
        permissions = self.repository_permission.find_by_id_rol( rol_id )
        
        return {
            "rol": rol,
            "permissions": permissions
        }