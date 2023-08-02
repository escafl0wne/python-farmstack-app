from fastapi import APIRouter

from modules.user_module.user_service import UserService

user_router = APIRouter(prefix="/users",tags=["users"])
user_service = UserService()

@user_router.get("test")
async def test():
    return user_service.test()

# class UserController:
#     def __init__(self) -> None:
#         self.router = APIRouter()
#         self.userService = UserService()
#         self.router.add_api_route("/", self.get_users, methods=["GET"])
#             # self.router.add_api_route("/", self.add_user, methods=["POST"])
#             # self.router.add_api_route("/{user_id}", self.delete_user, methods=["DELETE"])   
#     def get_router(self) -> APIRouter:
#         return self.router
        
#     async def get_users(self):
#         return self.userService.get_users("miro")