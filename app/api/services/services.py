from app.api.services.folders_service import FolderService
from app.api.services.hubs_service import HubsService
from app.api.services.items_service import ItemsService
from app.api.services.projects_service import ProjectsService
from app.api.services.version_service import VersionService
from app.api.services.retrieve_metadata_derivative_service import RetrieveMetadataDerivativeService
services = {
        "hubService": HubsService(),
        "projectsService": ProjectsService(),
        "folderService": FolderService(),
        "itemService": ItemsService(),
        "versionService": VersionService(),
        "derivativeService": RetrieveMetadataDerivativeService()        
    }