"""Extracted data model"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, func
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime


class Base(DeclarativeBase):
    pass


class ExtractedData(Base):
    """Model for storing extracted structured data"""
    __tablename__ = "extracted_data"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
    field_name = Column(String(100), nullable=False)
    field_value = Column(String(500))
    confidence_score = Column(Float, default=0.0)
    extraction_source = Column(String(50))  # ai, manual, etc.
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<ExtractedData(document_id={self.document_id}, field={self.field_name})>"
