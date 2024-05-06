# version_controller.py
from fastapi import APIRouter, Depends, HTTPException
from app.api.services.version_service import VersionService  # Ensure the import path matches your project structure

router = APIRouter()

# @router.get("/versions/{project_id}/{version_id}", response_model=list[str])
@router.get("/{project_id}/{version_id}")
async def get_versions(project_id: str, version_id: str, version_service: VersionService = Depends(VersionService)):
    try:
        versions = await version_service.get_versions(project_id, version_id)
        if versions is None:
            raise HTTPException(status_code=404, detail="No versions found")
        return versions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
