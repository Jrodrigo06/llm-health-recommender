from passlib.context import CryptContext
from jose import jwt, JWTError, ExpiredSignatureError
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

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
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")


# Method to create access token for 60 minutes
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (timedelta(minutes=60))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Decodes token
def decode_access_token(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except ExpiredSignatureError:
       print("Expired token")
       raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired. Please log in again.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except JWTError:
        # any other JWT-related error
        raise HTTPException(
           status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
          headers={"WWW-Authenticate": "Bearer"},
      )
# Method to get current user
def get_current_user(token: str = Depends(oauth2_scheme)) -> int:
    actual_token = decode_access_token(token)
    user_id = actual_token.get("user_id")
    if(user_id):
        return user_id
    else:
        raise HTTPException("Error in verifying token")
