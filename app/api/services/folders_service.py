from fastapi import FastAPI, HTTPException, Depends
import httpx
from app.urls import urls  # Adjust this import based on your actual project structure
from app.api.services.auth_service import AuthModule  # Adjust this import based on your actual project structure


class FolderService:
    def __init__(self):
        self.base_url = urls['APS_HOST_BASE_URL']
        self.get_hubs_url = urls['GET_HUBS_URL']
        self.get_projects_url = urls['GET_PROJECTS_URL']
        self.folders_url = urls['FOLDERS_URL']
        self.get_data_from_folders_url = urls['GET_DATA_FROM_FOLDERS_URL']
        self.auth_module = AuthModule()

    async def get_top_folders(self, hub_id: str, project_id: str):
        url = f"{self.base_url}{self.get_hubs_url}/{hub_id}{self.get_projects_url}/{project_id}/topFolders"
        token = await self.auth_module.get_token()
        if not token or not token.get('token'):
            raise HTTPException(status_code=400, detail="Failed to retrieve token")
        headers = {'Authorization': f"{token['token']}"}
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, headers=headers)
                response.raise_for_status()
                response_json =  response.json().get('data')

                return response_json
            except httpx.HTTPStatusError as e:
                raise HTTPException(status_code=e.response.status_code, detail=str(e))

    async def get_folder_content(self, project_id: str, folder_id: str):
        # print(f">>>>>>>>>>> {folder_id} <<<<<<<<<<")
        url = f"{self.base_url}{self.get_data_from_folders_url}/{project_id}{self.folders_url}/{folder_id}/contents"
        # print(url)
        token = await self.auth_module.get_token()
        # print(token)
        if not token or not token.get('token'):
            raise HTTPException(status_code=400, detail="Failed to retrieve token")
        headers = {'Authorization': f"{token['token']}"}
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, headers=headers)
                # print(response)
                response_json = response.json().get('data')
                # print(response_json)
                response.raise_for_status()
                
                return response_json
            except httpx.HTTPStatusError as e:
                raise HTTPException(status_code=e.response.status_code, detail=str(e))

folder_service = FolderService()