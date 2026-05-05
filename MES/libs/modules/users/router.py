from fastapi import APIRouter, Depends
from .schemas import UserCreate, UserResponse
from .service import UserService

router = APIRouter()

# Dependency Injection của FastAPI để dùng chung Service
def get_user_service():
    return UserService()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(user)

@router.get("/", response_model=list[UserResponse])
def get_users(service: UserService = Depends(get_user_service)):
    return service.get_users()
