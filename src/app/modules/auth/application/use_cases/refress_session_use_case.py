from app.modules.auth.domain.repositories.user_repository import UserRepository
from app.modules.setting.rol.domain.repositories.rol_repository import RolRepository
from app.modules.auth.domain.repositories.user_permission_repository import UserPermissionRepository
from app.core.security import (
    create_access_token, create_refress_token, verify_refress_token
)
from app.shared.exceptions.app_exception import AppException
from app.shared.constants.response_codes.auth_response_codes import AuthResponseCodes
from fastapi.encoders import jsonable_encoder

class RefressSessionUseCase():
    
    def __init__(self, repository_user: UserRepository, respository_rol: RolRepository, respository_permission: UserPermissionRepository ):
        self.repository_user = repository_user
        self.respository_rol = respository_rol
        self.respository_permission = respository_permission
        
    def execute( self , refress_token: str ):
        try:
            payload = verify_refress_token(refress_token )
            usua_Id = int(payload["usua_Id"])
            usua_RolId = int(payload["usua_RolId"])
            
            user_found = jsonable_encoder(self.repository_user.find_by_id( usua_Id ))
            rol_found = jsonable_encoder(self.respository_rol.find_by_id( usua_RolId ))
            permissions = self.respository_permission.find_all_by_id_user( usua_Id )
            
            payload_token = {
                "usua_Id": user_found["usua_Id"],
                "usua_Nombre": user_found["usua_Nombre"],
                "usua_RolId": user_found["usua_RolId"]
                
            }
            
            access_token_new = create_access_token( payload_token )
            refress_token_new = create_refress_token( payload_token )
            
            data = {
                "user": user_found,
                "rol": rol_found,
                "permissions": permissions,
                "accessToken": access_token_new,
                "refressToken": refress_token_new
            }
            
            return data
        
        except Exception:
            raise AppException(
                code=AuthResponseCodes.AUTH_NOT_AUTHORIZATION,
                message="Token no valido"
            )