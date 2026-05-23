
from dotenv import load_dotenv
import os
load_dotenv()

class Settings :
    
    APP_PORT = int(os.getenv("APP_PORT"))
    
    APP_NAME = os.getenv("APP_NAME")
    
    API_PREFIX = os.getenv("API_PREFIX")
    
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    
    MYSQL_PORT = os.getenv("MYSQL_PORT")
    
    MYSQL_USER = os.getenv("MYSQL_USER")
    
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    
    MYSQL_DB = os.getenv("MYSQL_DB")
    
    JWT_SECRET = os.getenv("JWT_SECRET")
    
    JWT_SECRET_REFRESS = os.getenv("JWT_SECRET_REFRESS")
    
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    

settings = Settings()