import pandas as pd
import asyncio
import os
from app.api.services.items_service import ItemsService

async def get_items_metadata(projectId, itemId, itemService:ItemsService):
  response = await (itemService.get_item_metadata(projectId, itemId))
 
  
  return pd.DataFrame(response)

async def get_items_metadata_version(projectId, itemId, itemService:ItemsService):
  return pd.DataFrame(await (itemService.get_item_version(projectId, itemId)))