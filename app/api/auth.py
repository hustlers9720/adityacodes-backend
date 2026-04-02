from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models import User
from app.schemas.user import UserIn
from app.core.security import create_access_token
from passlib.context import CryptContext

router = APIRouter(prefix="/api/v1/auth")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 🔐 Hash password
def hash_password(password: str):
    return pwd_context.hash(password)

# 🔐 Verify password
def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

# ✅ REGISTER
@router.post("/register")
def register(user: UserIn):
    db: Session = SessionLocal()

    # check if user already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # create new user
    new_user = User(
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()

    # create token
    token = create_access_token({"sub": user.email})

    return {"access_token": token}


# ✅ LOGIN
@router.post("/login")
def login(user: UserIn):
    db: Session = SessionLocal()

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="User not found")

    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid password")

    token = create_access_token({"sub": user.email})

    return {"access_token": token}