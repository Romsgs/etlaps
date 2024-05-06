from fastapi import FastAPI
import uvicorn
from app.api.routes.router import router

def create_app():
    app = FastAPI(
        title="balance-income-report",
        description="Balance Income Report API",
        version="1"
    )
    app.include_router(router=router)
    return app

if __name__ == '__main__':
    uvicorn.run("main:create_app", host='localhost', port=8080)
