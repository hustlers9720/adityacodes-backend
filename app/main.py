from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine
from app.api import auth, products, checkout
from app.db.seed import seed_products

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS (for React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(auth.router)
app.include_router(products.router)
app.include_router(checkout.router)

# ✅ Seed data on startup
@app.on_event("startup")
def startup_event():
    seed_products()