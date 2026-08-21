"""Authentication routes"""

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.core.dependencies import get_user_id
from app.schemas.schemas import UserCreate, UserLogin, UserResponse
from app.services.auth_service import create_user, authenticate_user, get_user_by_id, get_user_by_email

router = APIRouter(prefix="/api/auth", tags=["Authentication"])


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """Register a new user"""
    # Check if user already exists
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create the user
    db_user = create_user(db, user)
    return db_user


@router.post("/login")
def login(user: UserLogin, response: Response, db: Session = Depends(get_db)):
    """Login a user and set session cookie"""
    # Authenticate the user
    db_user = authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    # Set session cookie
    response.set_cookie(
        key="session_user_id",
        value=str(db_user.id),
        httponly=True,
        max_age=30 * 60 * 60,  # 30 hours
    )
    
    return {
        "message": "Login successful",
        "user_id": db_user.id,
        "email": db_user.email,
        "role": db_user.role,
    }


@router.post("/logout")
def logout(response: Response):
    """Logout a user by clearing session cookie"""
    response.delete_cookie("session_user_id")
    return {"message": "Logout successful"}


@router.get("/me", response_model=UserResponse)
def get_current_user(db: Session = Depends(get_db), user_id: int = Depends(get_user_id)):
    """Get current user information"""
    if user_id is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user
