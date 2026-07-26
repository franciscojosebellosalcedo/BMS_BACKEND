
from app.modules.menu.domain.entities.option_entity import OptionEntity
from app.modules.menu.domain.repositories.menu_repository import MenuRepository

class GetOptionsUseCase:
    
    def __init__(self, repository: MenuRepository ):
        self.repository = repository
        
    def execute(self):
        return self.repository.get_options()