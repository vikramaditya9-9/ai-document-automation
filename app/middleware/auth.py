"""Authentication middleware"""

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse


class SessionMiddleware(BaseHTTPMiddleware):
    """Middleware to extract user ID from session cookie"""

    async def dispatch(self, request: Request, call_next):
        # Extract user_id from session cookie
        user_id = request.cookies.get("session_user_id")
        
        # Add user_id to request state for use in dependencies
        if user_id:
            try:
                request.state.user_id = int(user_id)
            except (ValueError, TypeError):
                request.state.user_id = None
        else:
            request.state.user_id = None
        
        # Allow requests without auth to continue (routes will handle auth as needed)
        response = await call_next(request)
        return response
