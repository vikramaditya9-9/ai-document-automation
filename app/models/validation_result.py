"""Validation result model"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, func
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime


class Base(DeclarativeBase):
    pass


class ValidationResult(Base):
    """Model for storing validation results"""
    __tablename__ = "validation_results"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
    rule_name = Column(String(100), nullable=False)
    is_valid = Column(Boolean, default=False)
    severity = Column(String(50))  # critical, warning, info
    message = Column(String(500))
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<ValidationResult(document_id={self.document_id}, rule={self.rule_name})>"
