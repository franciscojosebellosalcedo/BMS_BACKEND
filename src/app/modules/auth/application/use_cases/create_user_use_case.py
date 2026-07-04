from app.modules.auth.domain.repositories.user_repository import UserRepository
from app.modules.auth.domain.repositories.user_permission_repository import UserPermissionRepository
from app.modules.auth.domain.types.create_user_input import CreateUserRequestInput
from app.shared.exceptions.app_exception import AppException
from app.shared.constants.response_codes.user_response_codes import UserResponseCodes
from app.core.security import hash_password

class CreateUserUseCase:

    def __init__(self, user_repository: UserRepository, permission_repository: UserPermissionRepository ):

        self.user_repository = user_repository
        self.permission_repository = permission_repository

    def execute(self, data: CreateUserRequestInput):

        values = data["user"]
        permissions = data["permissions"]
        
        user_found = self.user_repository.find_by_username(
            values["usua_NombreUsuario"]
        )

        if user_found:

            raise AppException(
                UserResponseCodes.USER_EXIST,
                "Usuario ya existe"
            )

        values["usua_Contrasenia"] = hash_password(
            values["usua_Contrasenia"]
        )
        
        user_created = self.user_repository.create_user(values)
        
        for permission in permissions:
            permission["peusua_UsuarioId"] = user_created.usua_Id
            
        permissions_created = self.permission_repository.save(user_created.usua_Id , permissions )

        return {
            "user": user_created,
            "permissions": permissions_created
        }