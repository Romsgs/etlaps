from fastapi import APIRouter, HTTPException
import httpx
import base64
from app.env_config import FULL_SCOPE, APS_CLIENT_ID, APS_CLIENT_SECRET
from app.urls import urls
import time

router = APIRouter()

class AuthModule:
    def __init__(self):
        self.base_url = urls['APS_HOST_BASE_URL']
        self.get_access_token_endpoint = urls['GET_ACCESS_TOKEN_ENDPOINT']
        self.full_scope = FULL_SCOPE
        self.client_id = APS_CLIENT_ID
        self.client_secret = APS_CLIENT_SECRET
        self.token_cache = {}
        self.set_headers()

    def set_headers(self):
        credentials = f"{self.client_id}:{self.client_secret}"
        authorization = base64.b64encode(credentials.encode()).decode('utf-8')
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'Authorization': f'Basic {authorization}'
        }

    def body(self):
        return {
            'grant_type': 'client_credentials',
            'scope': self.full_scope
        }

    async def get_token(self):
        if self.is_token_valid():
            return self.token_cache
        
        url = f"{self.base_url}{self.get_access_token_endpoint}"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, data=self.body(), headers=self.headers)
                response.raise_for_status()
                data = response.json()
                self.token_cache = {
                    'access_token': data['access_token'],
                    'token_type': data['token_type'],
                    'expires_in': data['expires_in'],
                    'token': f"{data['token_type']} {data['access_token']}",
                    'expires_at': time.time() + data['expires_in']
                }
                return self.token_cache
            except httpx.HTTPStatusError as e:
                raise HTTPException(status_code=e.response.status_code, detail=str(e))

    def is_token_valid(self):
        return self.token_cache and time.time() + 120 < self.token_cache['expires_at']

# # auth_module.py
# from fastapi import APIRouter, HTTPException, Depends
# import httpx
# import base64
# from app.env_config import FULL_SCOPE, APS_CLIENT_ID, APS_CLIENT_SECRET
# from app.urls import urls
# router = APIRouter()

# class AuthModule:
#     def __init__(self):
#         self.base_url = urls['APS_HOST_BASE_URL']
#         self.get_access_token_endpoint = urls['GET_ACCESS_TOKEN_ENDPOINT']
#         self.full_scope = FULL_SCOPE
#         self.client_id = APS_CLIENT_ID
#         self.client_secret = APS_CLIENT_SECRET

#     async def get_token(self):
#         url = f"{self.base_url}{self.get_access_token_endpoint}"
#         body = {
#             'grant_type': 'client_credentials',
#             'scope': self.full_scope
#         }
#         credentials = f"{self.client_id}:{self.client_secret}"
#         authorization = base64.b64encode(credentials.encode()).decode('utf-8')

#         headers = {
#             'Content-Type': 'application/x-www-form-urlencoded',
#             'Accept': 'application/json',
#             'Authorization': f'Basic {authorization}'
#         }

#         async with httpx.AsyncClient() as client:
#             try:
#                 response = await client.post(url, data=body, headers=headers)
#                 response.raise_for_status()  # Raises an exception for 4XX/5XX responses
#                 data = response.json()
#                 token_response = {
#                     'access_token': data['access_token'],
#                     'token_type': data['token_type'],
#                     'expires_in': data['expires_in'],
#                     'token': f"{data['token_type']} {data['access_token']}"
#                 }
#                 return token_response
#             except httpx.HTTPStatusError as e:
#                 raise HTTPException(status_code=e.response.status_code, detail=str(e))

# # Optional: Define a router endpoint if needed
# @router.post("/get_token")
# async def get_token_route(auth_module: AuthModule = Depends(AuthModule)):
#     return await auth_module.get_token()
