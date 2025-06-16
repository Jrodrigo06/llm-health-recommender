from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Method for hashing password 
def hash_password(password: str):
    return pwd_context.hash(password)

# Method for verifying password
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

SECRET_KEY = "Jeromes_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Method to create access token for 60 minutes
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + (timedelta(minutes=60))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])