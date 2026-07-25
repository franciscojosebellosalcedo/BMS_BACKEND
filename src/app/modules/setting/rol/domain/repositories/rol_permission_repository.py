
from abc import ABC
from app.modules.setting.rol.domain.types.save_rol_permission_input import SaveRolPermissionInput

class RolPermissionRepository (ABC ):
    
    def save(self, permissions: list[SaveRolPermissionInput]):
        pass
    
    def find_by_id_rol( self, rol_Id: int ):
        pass