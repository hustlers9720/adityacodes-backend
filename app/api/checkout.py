# app/api/checkout.py
from fastapi import APIRouter
from app.schemas.checkout import CheckoutIn

router = APIRouter(prefix="/api/v1/checkout")

@router.post("/")
def checkout(data: CheckoutIn):
    return {
        "id": 123,
        "status": "success"
    }