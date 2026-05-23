from passlib.context import CryptContext
from jose import jwt
from app.core.config import settings

password_context = CryptContext(
    schemes=["bcrypt"]
)

def hash_password (password: str ):
    return password_context.hash( password )

def verify_password( password: str , password_hash: str):
    return password_context.verify( password , password_hash )

def create_access_token( payload: dict):
    return jwt.encode(
        payload,
        settings.JWT_SECRET,
        settings.JWT_ALGORITHM
    )
    
def verify_token ( token: str ):
    return jwt.decode( token , settings.JWT_SECRET )

def verify_refress_token (refress_token: str):
    return jwt.decode( refress_token, settings.JWT_SECRET_REFRESS )
    
def create_refress_token( payload: dict):
    return jwt.encode(
        payload,
        settings.JWT_SECRET_REFRESS,
        settings.JWT_ALGORITHM
    )