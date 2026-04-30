from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import SessionLocal
from models.user import User
from schemas.user_schemas import UserCreate
from auth.password import hash_password

router = APIRouter()

# Database dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

# Register endpoint
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    # check email exists
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )
    
    # Hash password
    hashed_password = hash_password(user.password)

    # Create user object
    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password,
        slug=user.name.lower().replace(" ","-")
    )

    # Save to database
    db.add(new_user)

    # Commit changes
    db.commit()

    db.refresh(new_user)

    return {"message": "User registered"}