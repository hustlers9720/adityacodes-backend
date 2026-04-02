# app/schemas/product.py
from pydantic import BaseModel

class ProductOut(BaseModel):
    id: int
    title: str
    price: float

    class Config:
        from_attributes = True