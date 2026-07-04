
from sqlalchemy.orm import Session
from app.modules.setting.rol.infraestructure.persistence.rol_model import RolModel
from sqlalchemy import select

class RolSeed():
    
    @staticmethod
    def run(db: Session):
        
        try:
            
            roles = [
                {
                    "rol_Nombre": "Administrador",
                    "rol_Descripcion": "Acceso todal al sistema",
                    "rol_Codigo": "ADMIN",
                    "rol_CreacionId": 1
                }
            ]
            
            for rol in roles:
                
                stmt = select( RolModel ).where(
                    RolModel.rol_Codigo == rol["rol_Codigo"]
                )
                
                exist = db.execute(stmt ).scalar_one_or_none()
                if not exist:
                    
                    rol_new = RolModel(
                        rol_Nombre = rol["rol_Nombre"],
                        rol_Descripcion = rol["rol_Descripcion"],
                        rol_Codigo = rol["rol_Codigo"],
                        rol_CreacionId = rol["rol_CreacionId"]
                    )
                    
                    db.add(rol_new)
                    db.commit()
                    
            print("Seed users execute successfuly")
            
        except:
            print("Error seeder roles")
            
    