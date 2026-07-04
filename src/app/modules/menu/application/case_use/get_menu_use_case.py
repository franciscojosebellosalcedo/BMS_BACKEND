from app.modules.menu.domain.repositories.menu_repository import MenuRepository

class GetMenuUseCase ():
    
    def __init__(self, repository: MenuRepository ):
        self.repository = repository
        
    def execute(self):
        return self.repository.get_menu()