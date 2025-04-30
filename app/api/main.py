from fastapi import APIRouter

from app.api.routes import vibrate

api_router = APIRouter()
api_router.include_router(vibrate.router)

