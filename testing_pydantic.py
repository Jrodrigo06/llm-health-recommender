from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

# Create an instance of the User model w/ Pydantic
user = User(id=1, name='John Doe', email = 'hi@gmail.com')

user_data = {
    'id': 1,
    'name': 'John Doe',
    'email': 'hi@gmail.com'
}
# Create an instance of the User model w/ Pydantic using a dictionary
user2 = User(**user_data)
