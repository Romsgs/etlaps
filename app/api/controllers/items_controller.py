# items_controller.py
from app.api.services.items_service import ItemsService
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

@router.get("/metadata/{project_id}/{item_id}")
async def item_metadata(project_id: str, item_id: str, service: ItemsService = Depends(ItemsService)):
    try:
        return await service.get_item_metadata(project_id, item_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/version/{project_id}/{item_id}")
async def item_versions(project_id: str, item_id: str, service: ItemsService = Depends(ItemsService)):
    try:
        return await service.get_item_version(project_id, item_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
