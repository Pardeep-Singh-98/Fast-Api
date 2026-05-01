from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import SessionLocal
from models.user import User
from schemas.user_schemas import UserCreate, UserLogin
from auth.password import hash_password,verify_password
from auth.jwt_handler import create_refresh_token,create_access_token

from auth.dependencies import get_current_user


#insert refresh token
from models.refresh_token import RefreshToken
from config.settings import REFRESH_TOKEN_EXPIRE_DAYS
from datetime import datetime, timedelta

import hashlib

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

    # db.refresh(new_user)

    return {"message": "User registered"}


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    # check user exists
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    # verify password
    if not verify_password(
        user.password,
        existing_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    # create token
    token = create_access_token({
        "sub": str(existing_user.id),
        "email": existing_user.email,
    })

    refresh_token = create_refresh_token({
        "sub": str(existing_user.id),
        "email": existing_user.email,
    })

    # Expiration time
    expire = datetime.utcnow() + timedelta(
        days=REFRESH_TOKEN_EXPIRE_DAYS
    )
    
    # remove old refresh token
    db.query(RefreshToken).filter(
        RefreshToken.user_id == existing_user.id
    ).delete()

    db.commit()

    db_token = RefreshToken(
        user_id=existing_user.id,
        type='refresh',
        token=hash_token(refresh_token),
        expires_at=expire
    )

    db.add(db_token)
    db.commit()

    # return {"message":"Login is working"}
    return {
        "access_token": token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "user": {
            "id": existing_user.id,
            "name": existing_user.name,
            "email": existing_user.email,
        }
    }

def hash_token(token: str):
    return hashlib.sha256(token.encode()).hexdigest()
    

@router.get("/me")
def me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email
    }