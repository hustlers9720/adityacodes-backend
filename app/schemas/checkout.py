# app/schemas/checkout.py
from pydantic import BaseModel

class CheckoutIn(BaseModel):
    items: list