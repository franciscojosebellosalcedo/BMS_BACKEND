from app.modules.auth.domain.repositories.user_repository import UserRepository
from app.modules.auth.domain.types.create_user_input import CreateUserInput
from app.shared.exceptions.app_exception import AppException
from app.shared.constants.response_codes.user_response_codes import UserResponseCodes
from app.core.security import hash_password

class CreateUserUseCase:

    def __init__(self, repository: UserRepository):

        self.repository = repository

    def execute(self, values: CreateUserInput):

        user_found = self.repository.find_by_username(
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

        return self.repository.create_user(values)