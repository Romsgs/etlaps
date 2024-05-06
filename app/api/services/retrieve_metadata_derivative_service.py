import asyncio
from fastapi import HTTPException
import httpx
from app.urls import urls  
from app.api.services.auth_service import AuthModule  

class RetrieveMetadataDerivativeService:
  def __init__(self):
    self.base_url = urls['APS_HOST_BASE_URL']
    self.model_derivative_url = urls['MODEL_DERIVATIVE']
    self.auth_module = AuthModule()
    
    
  async def get_list_of_viewables(self, urnOfSouce):
    url = f"{self.base_url}{self.model_derivative_url}/{urnOfSouce}/metadata"
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

  async def get_object_hierarchy(self, url_safe_urn_of_source, dv_gui_0):
    url = f"{self.base_url}{self.model_derivative_url}/{url_safe_urn_of_source}/metadata/{dv_gui_0}"
    token = await self.auth_module.get_token()
    if not token or not token.get('token'):
        raise HTTPException(status_code=400, detail="Failed to retrieve token")
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
          
  async def get_properties(self, url_safe_urn_of_source, dv_gui_0):
    url = f"{self.base_url}{self.model_derivative_url}/{url_safe_urn_of_source}/metadata/{dv_gui_0}/properties"
    print(f"Usando essa url no Retrieve metadata derivative service: \n{url}")
    token = await self.auth_module.get_token()
    if not token or not token.get('token'):
        raise HTTPException(status_code=400, detail="Failed to retrieve token")
    if not token or not token.get('token'):
        raise HTTPException(status_code=400, detail="Failed to retrieve token")
    headers = {'Authorization': f"{token['token']}"}
    print(f"usando esse headers: {headers}")
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers)
            print(f"essa e a resposta {response}")
            response.raise_for_status()
            response_json =  response.json().get('data')
            return response_json
            
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))
          
# https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLnZjUzlmM19aVDR1T3VyQ2FKb2djUXc_dmVyc2lvbj0x/metadata/5389825b-b62e-4c07-ad20-326bfd3a3231
# https://developer.api.autodesk.com/modelderivative/v2/designdata/dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLnZjUzlmM19aVDR1T3VyQ2FKb2djUXc_dmVyc2lvbj0x/metadata/5389825b-b62e-4c07-ad20-326bfd3a3231/properties