from fastapi import FastAPI, HTTPException, Depends
import httpx
from app.api.services.auth_service import AuthModule  
from app.urls import urls  

app = FastAPI()

class VersionService:
    def __init__(self):
        self.base_url = urls['APS_HOST_BASE_URL']
        self.get_data_from_folders_url = urls['GET_DATA_FROM_FOLDERS_URL']
        self.auth_module = AuthModule()

    async def get_versions(self, project_id: str, version_id: str):
        url = f"{self.base_url}{self.get_data_from_folders_url}/{project_id}/versions/{version_id}"
        
        token = await self.auth_module.get_token()
        if not token or not token.get('token'):
            raise HTTPException(status_code=400, detail="Failed to retrieve token")
        
        headers = {'Authorization': f"{token['token']}"}
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, headers=headers)
                response.raise_for_status()
               
                return response.json().get('data')
            except httpx.HTTPStatusError as e:
                print(e.response.json()) 
                raise HTTPException(status_code=e.response.status_code, detail=str(e))

version_service = VersionService()
# https://developer.api.autodesk.com/data/v1/projects/b.2cd2ae33-69fd-4d41-8401-21457ebd8376/items/urn:adsk.wipprod:dm.lineage:6vo44vQ5QUyS3str8nGufw/versions