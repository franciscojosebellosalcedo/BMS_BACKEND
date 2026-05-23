from fastapi import Depends

from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.core.security import verify_token

from app.modules.auth.infraestructure.repositories.user_repository_impl import UserRepositoryImpl
from app.shared.exceptions.app_exception import AppException
from app.shared.constants.response_codes.auth_response_codes import AuthResponseCodes


security = HTTPBearer()

def get_current_user(

    credentials: HTTPAuthorizationCredentials = Depends(
        security
    ),

    db: Session = Depends(
        get_db
    )
):

    try:

        token = credentials.credentials

        payload = verify_token(
            token
        )

        usua_Id = int(
            payload["usua_Id"]
        )

        repository = UserRepositoryImpl(
            db
        )

        user = repository.find_by_id(
            usua_Id
        )

        if not user:

            raise AppException(
                code=AuthResponseCodes.AUTH_NOT_AUTHORIZATION,
                status_code=401,
                message="Usuario no encontrado"
            )

        if not user.usua_Activo:

            raise AppException(
                status_code=403,
                code=AuthResponseCodes.AUTH_NOT_AUTHORIZATION,
                message="Usuario inactivo"
            )

        return user

    except Exception:

        raise AppException(
            status_code=401,
            code=AuthResponseCodes.AUTH_NOT_AUTHORIZATION,
            message="Token inválido"
        )