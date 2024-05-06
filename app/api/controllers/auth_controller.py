from fastapi import APIRouter, HTTPException
from app.api.services.auth_service import AuthModule

auth_router = APIRouter()
auth_module = AuthModule()

@auth_router.post("/api/auth/get_token")
async def get_token():
    print('---------------------------')
    return await auth_module.get_token()

@auth_router.get("/auth/callback")
async def callback():
    return {"message": "HELLO"}
