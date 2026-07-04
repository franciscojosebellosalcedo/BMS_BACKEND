from sqlalchemy.orm import Session
from app.core.menu import menu
from app.modules.menu.infraestructure.persistence.module_model import ModuleModel
from app.modules.menu.infraestructure.persistence.submodule_model import SubmoduleModel
from app.modules.menu.infraestructure.persistence.option_model import OptionModel
from sqlalchemy import select, update

class MenuSeed:
    
    @staticmethod
    def run( db: Session ):
        
        for data in menu:
            
            module = data["module"]
            
            stmt = select( ModuleModel ).where( ModuleModel.modulo_Codigo == module["modulo_Codigo"])
            module_found = db.execute( stmt ).scalar_one_or_none()
            
            if not module_found:
                module_new = ModuleModel(
                    modulo_Nombre = module["modulo_Nombre"],
                    modulo_Codigo = module["modulo_Codigo"],
                    modulo_Indice = module["modulo_Indice"],
                    modulo_Activo = module["modulo_Activo"],
                )
                
                db.add(module_new )
                db.commit()
                db.refresh( module_new )
                
                module_found = module_new
                
            else:
                
                stmt_update_module = update( ModuleModel ).where(ModuleModel.modulo_Id == module_found.modulo_Id ).values(
                    modulo_Nombre = module_found.modulo_Nombre,
                    modulo_Activo = module_found.modulo_Activo,
                    modulo_Indice = module_found.modulo_Indice
                )
                db.execute(stmt_update_module)
                db.commit()
            
            if "submodules" in data:
                
                submodules = data["submodules"]
                
                for data_submodule in submodules:
                    
                    submodule = data_submodule["submodule"]
                    
                    stmt = select( SubmoduleModel ).where( SubmoduleModel.submo_Codigo == submodule["submo_Codigo"])
                    submodule_found = db.execute( stmt ).scalar_one_or_none()
                    
                    if not submodule_found : 
                        submodule_new = SubmoduleModel(
                            submo_Nombre = submodule["submo_Nombre"],
                            submo_Activo = submodule["submo_Activo"],
                            submo_Indice = submodule["submo_Indice"],
                            submo_Codigo = submodule["submo_Codigo"],
                            submo_ModuloId = module_found.modulo_Id
                        )
                        
                        db.add( submodule_new )
                        db.commit()
                        db.refresh( submodule_new )
                        
                        submodule_found = submodule_new
                        
                    else:
                        
                        stmt = update( SubmoduleModel ).where( SubmoduleModel.submo_Id == submodule_found.submo_Id ).values(
                            submo_Nombre = submodule["submo_Nombre"],
                            submo_Activo = submodule["submo_Activo"],
                            submo_Indice = submodule["submo_Indice"],
                        )
                        
                        db.execute( stmt )
                        db.commit()
                        
                        if "options" in data_submodule:
                            
                            options = data_submodule["options"]
                            
                            for option in options:
                                
                                stmt = select( OptionModel ).where( OptionModel.opci_Codigo == option["opci_Codigo"])
                                option_found = db.execute( stmt ).scalar_one_or_none()
                                
                                if not option_found:
                                    
                                    option_new = OptionModel(
                                        opci_Nombre = option["opci_Nombre"],
                                        opci_Codigo = option["opci_Codigo"],
                                        opci_SubmoduloId = submodule_found.submo_Id,
                                        opci_Activo = option["opci_Activo"],
                                        opci_Slug = option["opci_Slug"],
                                    )
                                    
                                    db.add( option_new )
                                    db.commit()
                                    db.refresh( option_new )
                                    
                                    option_found = option_new
                                    
                                else:
                                    
                                    stmt = update( OptionModel ).where( OptionModel.opci_Id == option_found.opci_Id ).values(
                                        opci_Nombre = option["opci_Nombre"],
                                        opci_Activo = option["opci_Activo"],
                                        opci_Slug = option["opci_Slug"],
                                        opci_Codigo = option["opci_Codigo"]
                                    )
                                    
                                    db.execute(stmt )
                                    db.commit()