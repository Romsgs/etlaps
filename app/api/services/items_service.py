from fastapi import FastAPI, HTTPException, Depends
import httpx
from app.urls import urls  
from app.api.services.auth_service import AuthModule  

app = FastAPI()

class ItemsService:
    def __init__(self):
        self.base_url = urls['APS_HOST_BASE_URL']
        self.get_data_from_folders_url = urls['GET_DATA_FROM_FOLDERS_URL']
        self.auth_module = AuthModule()  # Assuming AuthModule handles token authentication

    async def get_item_metadata(self, project_id: str, item_id: str):
        url = f"{self.base_url}{self.get_data_from_folders_url}/{project_id}/items/{item_id}"
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
                raise HTTPException(status_code=e.response.status_code, detail=str(e))

    async def get_item_version(self, project_id: str, item_id: str):
        url = f"{self.base_url}{self.get_data_from_folders_url}/{project_id}/items/{item_id}/versions"
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
                raise HTTPException(status_code=e.response.status_code, detail=str(e))

items_service = ItemsService()
