"""Document model"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Document(Base):
    """Document model for storing uploaded documents"""
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    original_filename = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=False)
    document_type = Column(String(50))  # invoice, po, contract, etc.
    status = Column(
        String(50),
        default="UPLOADED"
    )  # UPLOADED, PROCESSING, TEXT_EXTRACTED, DATA_EXTRACTED, VALIDATED, PENDING_REVIEW, APPROVED, REJECTED, FAILED
    uploaded_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Document(id={self.id}, filename={self.filename}, status={self.status})>"
