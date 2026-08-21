"""Document routes"""

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.core.dependencies import get_user_id
from app.schemas.schemas import DocumentResponse
from app.services.document_service import save_upload_file, get_document, get_user_documents, delete_document

router = APIRouter(prefix="/api/documents", tags=["Documents"])


@router.post("/upload", response_model=DocumentResponse)
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user_id: int = Depends(get_user_id),
):
    """Upload a new document"""
    if user_id is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    # Validate file
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file selected")
    
    # Save the document
    document = save_upload_file(file, user_id, db)
    return document


@router.get("/", response_model=list[DocumentResponse])
def list_documents(db: Session = Depends(get_db), user_id: int = Depends(get_user_id)):
    """Get all documents for the current user"""
    if user_id is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    documents = get_user_documents(db, user_id)
    return documents


@router.get("/{document_id}", response_model=DocumentResponse)
def get_document_details(
    document_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_user_id),
):
    """Get details of a specific document"""
    if user_id is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    document = get_document(db, document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    
    # Check ownership
    if document.uploaded_by != user_id:
        raise HTTPException(status_code=403, detail="Access denied")
    
    return document


@router.delete("/{document_id}")
def delete_document_endpoint(
    document_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_user_id),
):
    """Delete a document"""
    if user_id is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    success = delete_document(db, document_id, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Document not found or access denied")
    
    return {"message": "Document deleted successfully"}
