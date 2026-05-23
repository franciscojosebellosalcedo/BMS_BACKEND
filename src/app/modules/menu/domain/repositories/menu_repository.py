
from abc import ABC, abstractmethod

class MenuRepository ( ABC ):
    
    @abstractmethod
    def get_menu():
        pass