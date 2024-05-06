# hubs_controller.py
from fastapi import APIRouter, Depends, HTTPException, Path
from app.api.services.hubs_service import HubsService  # Ensure the import path matches your project structure

router = APIRouter()

@router.get("/", response_model=list[str])
async def get_all_hubs(hubs_service: HubsService = Depends(HubsService)):
    try:
        return await hubs_service.get_all_hubs()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{hub_id}")
async def get_hub(hub_id: str, hubs_service: HubsService = Depends(HubsService)):
    try:
        return await hubs_service.get_specific_hub(hub_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
