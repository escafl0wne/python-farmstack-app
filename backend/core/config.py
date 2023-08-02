from pydantic import BaseSettings,AnyHttpUrl
from decouple import config




class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY",cast=str)
    JWT_REFRESH_KEY: str = config("JWT_REFRESH_KEY",cast=str)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRATION: int = 15 # 7 days
    REFRESH_TOKEN_EXPIRATION: int = 60 * 24 * 7 # 7 days
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []
    PROJECT_NAME: str = "ANIMELIST"
    
    #Database
    MONGO_URI: str = config("MONGO_URI",cast=str)
    
class Config:
    case_sensitive = True
    env_file = ".env"
settings = Settings()