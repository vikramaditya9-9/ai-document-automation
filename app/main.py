"""Main FastAPI application"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from app.core.config import settings
from app.middleware.auth import SessionMiddleware
from app.api.routes import router as api_router
from app.database.session import engine
from app.models.user import Base

# Create FastAPI application
app = FastAPI(
    title=settings.app_name,
    description="AI-powered document workflow automation platform",
    version="0.1.0",
    debug=settings.debug,
)

# Add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SessionMiddleware)

# Mount static files (CSS, JS, images, etc.)
static_dir = Path(__file__).parent / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# Include API routes
app.include_router(api_router)


# Create database tables
@app.on_event("startup")
def create_tables():
    """Create database tables on startup"""
    Base.metadata.create_all(bind=engine)


# Serve frontend
@app.get("/")
async def serve_frontend():
    """Serve the main frontend application"""
    templates_dir = Path(__file__).parent / "templates"
    index_file = templates_dir / "index.html"
    
    if index_file.exists():
        return FileResponse(str(index_file))
    else:
        return JSONResponse({
            "message": "Welcome to DocuFlow AI",
            "documentation": "/docs",
            "health": "/health",
        })


# Health Check Endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify the application is running.
    
    Returns:
        dict: Status information
    """
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "application": settings.app_name,
            "version": "0.1.0",
        },
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
    )
