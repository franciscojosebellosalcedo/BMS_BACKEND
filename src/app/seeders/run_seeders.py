from app.seeders.user_seed import UserSeed
from app.seeders.rol_seed import RolSeed
from app.core.database import SessionLocal
from app.seeders.menu_seed import MenuSeed

def run():
    
    db = SessionLocal()
    
    try:
        
        UserSeed.run( db )
        RolSeed.run( db )
        MenuSeed.run( db )
        
    finally:
        db.close()
        