
from fastapi import FastAPI
from core.config import settings
from core.database import init_db
from modules.user_module.user_controller import user_router


app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.on_event("startup")
async def startup_event():
    """
    Code snippet from config.py
    initialise crucial application services
    """
    await init_db()
    
app.include_router(user_router,prefix=settings.API_V1_STR)
   

