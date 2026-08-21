"""Workflow history model"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime


class Base(DeclarativeBase):
    pass


class WorkflowHistory(Base):
    """Model for tracking document workflow transitions"""
    __tablename__ = "workflow_history"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
    previous_status = Column(String(50))
    new_status = Column(String(50), nullable=False)
    performed_by = Column(Integer, ForeignKey("users.id"))
    comments = Column(String(500))
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<WorkflowHistory(document_id={self.document_id}, status={self.new_status})>"
