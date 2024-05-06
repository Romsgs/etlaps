# projects_controller.py
from fastapi import APIRouter, Depends, HTTPException, Path
from app.api.services.projects_service import ProjectsService  # Ensure the import path matches your project structure

router = APIRouter()

# @router.get("/projects/{hub_id}", response_model=list[str])
@router.get("/{hub_id}")
async def get_all_projects(hub_id: str, projects_service: ProjectsService = Depends(ProjectsService)):
    try:
        projects = await projects_service.get_all_projects(hub_id)
        if not projects:
            raise HTTPException(status_code=404, detail="No projects found")
        return projects
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{hub_id}/{project_id}")
async def get_project(hub_id: str, project_id: str, projects_service: ProjectsService = Depends(ProjectsService)):
    try:
        project = await projects_service.get_specific_project(hub_id, project_id)
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        return project
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
