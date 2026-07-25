from app.modules.auth.infraestructure.repositories.user_repository_impl import UserRepositoryImpl
from app.modules.auth.infraestructure.repositories.user_permission_repository_impl import UserPermissionRepositoryImpl
from app.modules.auth.application.use_cases.create_user_use_case import CreateUserUseCase
from factories.user_factory import data_create_user

def test_create_user_use_case( db_session ):
    
    repository_user = UserRepositoryImpl( db_session )
    
    repository_permissions = UserPermissionRepositoryImpl( db_session )
    
    use_case = CreateUserUseCase( repository_user, repository_permissions )
    
    data = data_create_user()

    created = use_case.execute(data)
    
    assert created["user"] is not None