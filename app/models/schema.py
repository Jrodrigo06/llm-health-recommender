from pydantic import BaseModel

"""
This model defines the schema for user information and requests.
"""

class UserInfo(BaseModel):
    name: str
    email: str
    age: int
    bmi: float
    height: float
    weight: float
    diabetes: bool
    overweight: bool
    heart_disease: bool
    family_history: str
    smoking: bool
    alcohol: bool

class UserRequest(BaseModel):
    question: str
    

class UserSignUp(BaseModel):
    user_id: int
    password: str
    user_info: UserInfo