import pandas as pd
import asyncio
import os
from app.api.services.version_service import VersionService

async def get_items_version(project_id, version_id, versionService:VersionService):
  items_metadata = pd.DataFrame(await (versionService.get_versions(project_id, version_id)))
  
  return items_metadata