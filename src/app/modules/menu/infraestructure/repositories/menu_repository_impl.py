from app.modules.menu.domain.repositories.menu_repository import MenuRepository
from sqlalchemy.orm import Session
from app.modules.menu.infraestructure.persistence.module_model import ModuleModel
from app.modules.menu.infraestructure.persistence.submodule_model import SubmoduleModel
from app.modules.menu.infraestructure.persistence.option_model import OptionModel
from sqlalchemy import select

class MenuRepositoryImpl( MenuRepository ):
    
    def __init__(
        self,
        db: Session
    ):
        self.db = db
        
    def get_options(self):
        
        stmt = select( OptionModel )
        return self.db.execute( stmt ).scalars().all()
        
        
    def get_menu(self):
        
        stmt = select( ModuleModel )
        modules = self.db.execute(stmt).scalars().all()
        
        menu = []
        
        for module in modules:
            
            data = dict()
            
            data["module"] = module
            data["submodules"] = []
            
            stmt_submo = select( SubmoduleModel ).where( SubmoduleModel.submo_ModuloId == module.modulo_Id )
            submodules = self.db.execute( stmt_submo ).scalars().all()
            
            data_submo = dict()
            
            for submodule in submodules:
                data_submo["submodule"] = submodule
                
                stmt_options = select( OptionModel ).where( OptionModel.opci_SubmoduloId == submodule.submo_Id )
                options = self.db.execute( stmt_options ).scalars().all()
                data_submo["options"] = options
            
            data["submodules"].append( data_submo )
            
            menu.append( data )
            
        return menu