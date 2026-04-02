from fastapi import APIRouter
from app.db.database import SessionLocal
from app.db.models import Product
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1/products")

class ProductIn(BaseModel):
    title: str
    price: int


@router.get("/")
def get_products():
    db = SessionLocal()
    try:
        products = db.query(Product).all()
        return [
            {"id": p.id, "title": p.title, "price": p.price}
            for p in products
        ]
    finally:
        db.close()

#  ADD PRODUCT (UPDATED ROUTE)
@router.post("/add")
def add_product(product: ProductIn):
    db = SessionLocal()

    new_product = Product(
        title=product.title,
        price=product.price
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return {
        "id": new_product.id,
        "title": new_product.title,
        "price": new_product.price
    }