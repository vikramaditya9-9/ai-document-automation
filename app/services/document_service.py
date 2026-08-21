"""Document service"""

import os
import shutil
from pathlib import Path
from sqlalchemy.orm import Session
from app.models.document import Document
from app.core.config import settings


def save_upload_file(file, uploaded_by_id: int, db: Session) -> Document:
    """Save an uploaded file and create a document record"""
    
    # Create uploads directory if it doesn't exist
    upload_dir = Path(settings.upload_directory)
    upload_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate a unique filename
    original_filename = file.filename
    file_extension = Path(original_filename).suffix
    filename = f"{uploaded_by_id}_{Path(original_filename).stem}_{int(__import__('time').time())}{file_extension}"
    file_path = str(upload_dir / filename)
    
    # Save the file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Create document record
    db_document = Document(
        filename=filename,
        original_filename=original_filename,
        file_path=file_path,
        status="UPLOADED",
        uploaded_by=uploaded_by_id,
    )
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    
    return db_document


def get_document(db: Session, document_id: int):
    """Get a document by ID"""
    return db.query(Document).filter(Document.id == document_id).first()


def get_user_documents(db: Session, user_id: int):
    """Get all documents for a user"""
    return db.query(Document).filter(Document.uploaded_by == user_id).all()


def delete_document(db: Session, document_id: int, user_id: int) -> bool:
    """Delete a document (only by owner)"""
    document = db.query(Document).filter(
        Document.id == document_id,
        Document.uploaded_by == user_id
    ).first()
    
    if not document:
        return False
    
    # Delete the file
    if os.path.exists(document.file_path):
        os.remove(document.file_path)
    
    # Delete the database record
    db.delete(document)
    db.commit()
    
    return True
