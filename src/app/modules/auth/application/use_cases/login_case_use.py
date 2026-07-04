from app.modules.auth.domain.repositories.user_repository import UserRepository
from app.modules.setting.rol.domain.repositories.rol_repository import RolRepository
from app.modules.auth.domain.repositories.user_permission_repository import UserPermissionRepository
from app.modules.auth.domain.types.login_input import LoginInput
from app.core.security import ( verify_password, create_refress_token, create_access_token )
from app.shared.exceptions.app_exception import AppException
from app.shared.constants.response_codes.auth_response_codes import AuthResponseCodes

class LoginCaseUse:
    
    def __init__(
            self, 
            repository_user: UserRepository,
            repository_rol: RolRepository,
            repository_permission: UserPermissionRepository
        ):
        self.repository_user = repository_user
        self.repository_rol = repository_rol
        self.repository_permission = repository_permission
    
    def execute(self , values: LoginInput):
        
        user_found = self.repository_user.find_by_username( values['usua_NombreUsuario'] )
        
        if not user_found:
            raise AppException(
                code=AuthResponseCodes.AUTH_INVALID_CREDENTIALS,
                message="Credenciales no válidas"
            )
            
        if not user_found.usua_Activo:
            raise AppException(
                code=AuthResponseCodes.AUTH_USER_DISABLE,
                message="Usuario deshabilitado"
            )
        
        password_valid = verify_password( values["usua_Contrasenia"], user_found.usua_Contrasenia )
        
        if not password_valid:
            raise AppException(
                code=AuthResponseCodes.AUTH_INVALID_CREDENTIALS,
                message="Credenciales no válidas"
            )
        
        payload = {
            "usua_Id": user_found.usua_Id,
            "usua_Nombre": user_found.usua_Nombre,
            "usua_RolId": user_found.usua_RolId
        }
        
        access_token = create_access_token( payload )
        refress_token = create_refress_token( payload )
        
        rol_found = self.repository_rol.find_by_id(user_found.usua_RolId)
        permissions = self.repository_permission.find_all_by_id_user(user_found.usua_Id )
        
        data = {
            "user": user_found,
            "rol": rol_found,
            "permissions": permissions,
            "accessToken": access_token,
            "refressToken": refress_token
        }
        
        return data