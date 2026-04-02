# app/db/models.py
from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Float)

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)