import datetime
from beanie import Document,Indexed
from uuid import UUID, uuid4
from pydantic import Field,EmailStr




class User(Document):
    user_id: UUID = Field(default_factory=uuid4)
    username: str = Indexed(str,unique=True)
    email: Indexed(EmailStr,unique=True)
    hashed_password: str
    last_name: str
    first_name: str
    disabled: bool = False
    createdAt: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    
    # def __repr__(self):
    #     return f"<User {self.username}>"
    
    # def __str__(self):
    #     return f"<User {self.username}>"
    
    # def __hash__(self):
    #     return hash(self.username)
    
    # def __eq__(self, other:object)-> bool:
    #     if isinstance(other, User):
    #         return self.email == other.email
        
    #     return False
    
    # @property
    # def create(self)-> datetime:
    #     return self.id_generation_time

    # @classmethod
    # async def by_email(self,email:str)->"User":
    #     return await self.find_one({"email":email})

    class Settings:
        name="users_collection"