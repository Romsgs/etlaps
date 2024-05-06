# items_router.py
from fastapi import APIRouter
from app.api.controllers.items_controller import router as items_router
from app.api.controllers.projects_controller import router as project_router
from app.api.controllers.hubs_controller import router as hubs_router
from app.api.controllers.folders_controller import router as folders_router
from app.api.controllers.version_controller import router as versions_router
from app.api.controllers.auth_controller import auth_router

router = APIRouter()

router.include_router(items_router, prefix="/items", tags=["Items"])
router.include_router(project_router, prefix='/projects', tags=["projects"])
router.include_router(hubs_router, prefix='/hubs', tags=["hubs"])
router.include_router(folders_router, prefix='/folders', tags=["folders"])
router.include_router(versions_router, prefix='/versions', tags=["versions"])
router.include_router(auth_router, prefix='/api', tags=["api"])