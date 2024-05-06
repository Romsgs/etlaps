# folder_controller.py
from fastapi import APIRouter, Depends, HTTPException
from app.api.services.folders_service import FolderService  # Ensure the import path matches your project structure

router = APIRouter()

@router.get("/top_folders/{hub_id}/{project_id}")
async def get_top_folders(hub_id: str, project_id: str, folder_service: FolderService = Depends(FolderService)):
    try:
        return await folder_service.get_top_folders(hub_id, project_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/folder_content/{project_id}/{folder_id}")
async def get_folder_content(project_id: str, folder_id: str, folder_service: FolderService = Depends(FolderService)):
    try:
        return await folder_service.get_folder_content(project_id, folder_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 