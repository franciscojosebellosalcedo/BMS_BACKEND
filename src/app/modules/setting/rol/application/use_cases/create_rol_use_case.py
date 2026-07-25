
from app.modules.setting.rol.domain.repositories.rol_repository import RolRepository
from app.modules.setting.rol.domain.types.create_rol_input import CreateRolInput
from app.shared.exceptions.app_exception import AppException
from app.shared.constants.response_codes.rol_response_codes import RolResponseCodes
from app.modules.setting.rol.domain.repositories.rol_permission_repository import RolPermissionRepository
from app.modules.auth.domain.entities.user_entity import UserEntity

class CreateRolUseCase():
    
    def __init__(self, current_user: UserEntity,  repository_rol: RolRepository , repository_permission: RolPermissionRepository):
        
        self.repository_rol = repository_rol
        self.current_user = current_user
        self.repository_permission = repository_permission
        
    def execute(self, data: CreateRolInput):
        
        rol = data["rol"]
        rol["rol_CreacionId"] = self.current_user.usua_Id
        
        permissions = data["permissions"]
        
        if not len(permissions):
            raise AppException(
                RolResponseCodes.ROL_PERMISSION_EMPTY,
                "Se requiere los permisos"
            )
        
        exist = self.repository_rol.find_by_name( rol["rol_Nombre"] )
        
        if not exist:
            
            rol_created = self.repository_rol.create(rol)
            rol_Id = rol_created.rol_Id
            
            for permission in permissions:
                permission["perol_CreacionId"] = self.current_user.usua_Id
                permission["perol_RolId"] = rol_Id
            
            self.repository_permission.save( permissions )
            permission_saved = self.repository_permission.find_by_id_rol( rol_Id )
            
            return  {
                "rol": rol_created,
                "permissions": permission_saved
            }
        
        raise AppException(
            RolResponseCodes.ROL_EXIST,
            f"Rol de nombre {rol['rol_Nombre']} ya existe"
        )