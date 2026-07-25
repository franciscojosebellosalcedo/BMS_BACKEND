from pydantic import BaseModel

class SaveRolPermissionSchema( BaseModel ):
    perol_RolId: int | None = None
    perol_OpcionId: int
    perol_Crear: bool
    perol_Editar: bool
    perol_CambiarEstado: bool
    perol_CreacionId: int | None = None
    perol_ModificacionId: int | None = None