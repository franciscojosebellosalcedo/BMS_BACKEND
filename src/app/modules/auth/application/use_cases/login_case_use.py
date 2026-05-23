from app.modules.auth.domain.repositories.user_repository import UserRepository
from app.modules.auth.domain.repositories.rol_repository import RolRepository
from app.modules.auth.domain.types.login_input import LoginInput
from app.core.security import ( verify_password, create_refress_token, create_access_token )
from app.shared.exceptions.app_exception import AppException
from app.shared.constants.response_codes.auth_response_codes import AuthResponseCodes

class LoginCaseUse:
    
    def __init__(
            self, 
            repositoryUser: UserRepository,
            repositoryRol: RolRepository
        ):
        self.repositoryUser = repositoryUser
        self.repositoryRol = repositoryRol
    
    def execute(self , values: LoginInput):
        
        user_found = self.repositoryUser.find_by_username( values['usua_NombreUsuario'] )
        
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
        
        rol_found = self.repositoryRol.find_by_id(user_found.usua_RolId)
        
        data = {
            "user": user_found,
            "rol": rol_found,
            "accessToken": access_token,
            "refressToken": refress_token
        }
        
        return data