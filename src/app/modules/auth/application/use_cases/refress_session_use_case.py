from app.modules.auth.domain.repositories.user_repository import UserRepository
from app.modules.auth.domain.repositories.rol_repository import RolRepository
from app.core.security import (
    create_access_token, create_refress_token, verify_refress_token
)
from app.shared.exceptions.app_exception import AppException
from app.shared.constants.response_codes.auth_response_codes import AuthResponseCodes
from fastapi.encoders import jsonable_encoder

class RefressSessionUseCase():
    
    def __init__(self, repositoryUser: UserRepository, respositoryRol: RolRepository ):
        self.repositoryUser = repositoryUser
        self.respositoryRol = respositoryRol
        
    def execute( self , refress_token: str ):
        try:
            payload = verify_refress_token(refress_token )
            usua_Id = int(payload["usua_Id"])
            usua_RolId = int(payload["usua_RolId"])
            
            user_found = jsonable_encoder(self.repositoryUser.find_by_id( usua_Id ))
            rol_found = jsonable_encoder(self.respositoryRol.find_by_id( usua_RolId ))
            
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
                "accessToken": access_token_new,
                "refressToken": refress_token_new
            }
            
            return data
        
        except Exception:
            raise AppException(
                code=AuthResponseCodes.AUTH_NOT_AUTHORIZATION,
                message="Token no valido"
            )