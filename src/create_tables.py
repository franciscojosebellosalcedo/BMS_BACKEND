
from app.core.database import Base
from app.core.database import engine

from app.modules.auth.infraestructure.persistence.user_model import UserModel
from app.modules.setting.rol.infraestructure.persistence.rol_model import RolModel
from app.modules.menu.infraestructure.persistence.module_model import ModuleModel
from app.modules.menu.infraestructure.persistence.submodule_model import SubmoduleModel
from app.modules.menu.infraestructure.persistence.option_model import OptionModel
from app.modules.auth.infraestructure.persistence.user_permission_model import UserPermissionModel

def create_tables():

    Base.metadata.create_all(
        bind=engine
    )