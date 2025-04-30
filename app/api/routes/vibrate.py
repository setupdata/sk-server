from fastapi import APIRouter

from app.api.deps import http_ok

router = APIRouter(prefix="/vibrate", tags=["vibrate"])


@router.get("/")
async def read_items():
    return http_ok("hello vibrate")
