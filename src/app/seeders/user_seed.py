from sqlalchemy.orm import Session
from app.modules.auth.infraestructure.persistence.user_model import UserModel
from sqlalchemy import select
from app.core.security import hash_password

class UserSeed():
    
    @staticmethod
    def run( db: Session ):
        
        try:
            users = [
                {
                    "usua_Nombre": "Administrador",
                    "usua_NombreUsuario": "admin",
                    "usua_Contrasenia": "admin2026",
                    "usua_RolId": 1,
                    "usua_CreacionId": 1,
                    "usua_ModificacionId": 1
                }
            ]
        
            for user in users:
                stmt = select( UserModel ).where(
                    UserModel.usua_NombreUsuario == user["usua_NombreUsuario"]
                )
                
                exist = db.execute( stmt ).scalar_one_or_none()
                
                if not exist:
                    user["usua_Contrasenia"] = hash_password( user["usua_Contrasenia"])
                    
                    user_new = UserModel(
                        usua_Nombre = user["usua_Nombre"],
                        usua_NombreUsuario = user["usua_NombreUsuario"],
                        usua_Contrasenia = user["usua_Contrasenia"],
                        usua_RolId = user["usua_RolId"],
                        usua_CreacionId = user["usua_CreacionId"],
                        usua_ModificacionId = user["usua_ModificacionId"],
                    )
                    
                    db.add(user_new)
                    db.commit()
                    
                print("Seed users execute successfuly")
                
        except:
            
            print("Error Seed users")
