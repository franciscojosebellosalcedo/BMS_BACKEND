import uvicorn
from app.core.config import settings
from app.seeders.run_seeders import run

if __name__ == "__main__":

    uvicorn.run(
        "app.main:app",
        host="localhost",
        port=settings.APP_PORT,
        reload=True
    )
    
run()