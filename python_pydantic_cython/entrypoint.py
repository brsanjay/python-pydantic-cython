import pydantic
from pydantic import BaseModel

print("Hello world")
print('compiled: ', pydantic.compiled)

class User(BaseModel):
    id: int
    name = 'Jane Doe'

user = User(id='123')
print(user)