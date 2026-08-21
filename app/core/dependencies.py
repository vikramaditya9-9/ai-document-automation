"""Application dependencies"""

from fastapi import Request, Depends
from sqlalchemy.orm import Session
from app.database.session import SessionLocal


def get_db():
    """Dependency to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_id(request: Request) -> int:
    """Dependency to get user ID from session cookie"""
    user_id = getattr(request.state, "user_id", None)
    return user_id
