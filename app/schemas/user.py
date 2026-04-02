# app/schemas/user.py
from pydantic import BaseModel

class UserIn(BaseModel):
    email: str
    password: str