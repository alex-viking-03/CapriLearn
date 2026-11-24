from fastapi import APIRouter, Depends, HTTPException, Header

from sqlalchemy.orm import Session

from DTOs.UserDTO import ChangeUserRoleDTO, UserDTO, RegisterDTO
from Database import get_db
from Services.AdminService import create_first_admin, change_user_role as change_user_role_service
from Enums.UserRole import UserRole
from Models.User import User

router = APIRouter(
    prefix = "/api/admin",
    tags = ["Admin"])

@router.post("/setup", response_model = UserDTO)
def setup_admin(request: RegisterDTO,
                db: Session = Depends(get_db)):
    admin = create_first_admin(request, db)
    if admin == "username_exists":
        raise HTTPException(409, "Such username already exists")
    
    if admin == "email_exists":
        raise HTTPException(409, "Such email already exists")

    if admin == "admin_exists":
        raise HTTPException(403, "Admin is already exists")
    
    return UserDTO.model_validate(admin)

@router.put("/users/{user_id}/role", response_model=UserDTO)
def change_user_role(user_id: int,
                     role: ChangeUserRoleDTO,
                     admin_id: int = Header(...,alias="X-User-Id"),
                     db: Session = Depends(get_db)):
    user = change_user_role_service(user_id, role.role, admin_id, db)

    match user:
        case "admin_not_found":
            raise HTTPException(404, "Admin not found")

        case "forbidden":
            raise HTTPException(403, "Admin is deactivated")
    
        case "invalid_role":
            raise HTTPException(400, "Invalid role")

        case "user_not_found":
            raise HTTPException(404, "User not found")

        case "cannot_change_own_role":
            raise HTTPException(400, "Cannot change own role")

        case "last_admin":
            raise HTTPException(400, "Last admin remaining")

        case User() as user:
            return UserDTO.model_validate(user)

        case _:
            raise HTTPException(400, "Unknown error")