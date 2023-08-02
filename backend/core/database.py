from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models.user_model import User

from core.config import settings


async def init_db():
    db_client = AsyncIOMotorClient(settings.MONGO_URI)
    
    await init_beanie(
         database=db_client.db_name,
        document_models=[User]
        
    )