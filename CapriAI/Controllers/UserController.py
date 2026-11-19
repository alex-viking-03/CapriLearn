from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from DTOs.UserDTO import UserDTO, RegisterDTO, LogInDTO
from Database import get_db
from Services.UserService import register_user, login_user
router = APIRouter(
    prefix="/api/users",
    tags=["Users"])

@router.post("/register", response_model=UserDTO)
def register(request: RegisterDTO,
             db: Session = Depends(get_db)):
    user = register_user(request, db)

    if user == "email_exists":
        raise HTTPException(409, "User with such email is already exists")
    elif user == "username_exists":
        raise HTTPException(409, "User with such username is already exists")

    return UserDTO.model_validate(user)

@router.post("/login", response_model=UserDTO)
def login(request: LogInDTO,
          db: Session = Depends(get_db)):
    user = login_user(request, db)

    if user is None:
        raise HTTPException(401, "Invalid email or password")

    return UserDTO.model_validate(user)