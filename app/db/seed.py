from app.db.database import SessionLocal
from app.db.models import Product

def seed_products():
    db = SessionLocal()

    # check if already data exists
    existing = db.query(Product).first()
    if existing:
        db.close()
        return

    products = [
        Product(title="Laptop", price=50000),
        Product(title="Phone", price=20000),
        Product(title="Headphones", price=3000),
    ]

    db.add_all(products)
    db.commit()
    db.close()