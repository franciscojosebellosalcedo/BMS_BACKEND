from app.seeders.user_seed import UserSeed
from app.seeders.rol_seed import RolSeed
from app.core.database import SessionLocal

def run():
    
    db = SessionLocal()
    
    try:
        
        UserSeed.run( db )
        RolSeed.run( db )
        
    finally:
        db.close()
        