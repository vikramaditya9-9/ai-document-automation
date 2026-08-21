"""Pydantic schemas"""

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# User Schemas
class UserBase(BaseModel):
    email: EmailStr
    full_name: str


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(UserBase):
    id: int
    role: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


# Document Schemas
class DocumentBase(BaseModel):
    filename: str
    original_filename: str
    document_type: Optional[str] = None


class DocumentCreate(DocumentBase):
    pass


class DocumentResponse(DocumentBase):
    id: int
    file_path: str
    status: str
    uploaded_by: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Extracted Data Schemas
class ExtractedDataResponse(BaseModel):
    id: int
    document_id: int
    field_name: str
    field_value: Optional[str]
    confidence_score: float

    class Config:
        from_attributes = True


# Validation Result Schemas
class ValidationResultResponse(BaseModel):
    id: int
    document_id: int
    rule_name: str
    is_valid: bool
    severity: str
    message: Optional[str]

    class Config:
        from_attributes = True
