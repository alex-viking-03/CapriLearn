from sqlalchemy.orm import Session
from sqlalchemy import select, func

from Models.User import User
from Enums.UserRole import UserRole
from DTOs.UserDTO import RegisterDTO

from Services.UserService import get_user_by_email, get_user_by_username
from Security.PasswordHasher import hash_password

def admin_exists(db: Session):
    return db.scalar(select(User).where(User.role == UserRole.ADMIN))

def get_admin_by_id(admin_id: int, db: Session):
    return db.scalar(select(User)
                      .where(User.role == UserRole.ADMIN)
                      .where(User.id == admin_id))

def create_first_admin(request: RegisterDTO,
                       db: Session):
    if get_user_by_email(request.email, db) is not None:
        return "email_exists"
    if get_user_by_username(request.username, db) is not None:
        return "username_exists"

    admin = admin_exists(db)

    if admin is not None:
        return "admin_exists"

    admin = User(
        username = request.username,
        email = request.email,
        password_hash = hash_password(request.password),
        role = UserRole.ADMIN)

    try:
        db.add(admin)
        db.commit()
        db.refresh(admin)
    except Exception:
        db.rollback()
        raise

    return admin

def change_user_role(user_id: int, role: UserRole, admin_id: int, db: Session):
    admin = get_admin_by_id(admin_id, db)

    if admin is None:
        return "admin_not_found"
    elif not admin.is_active:
        return "forbidden"

    user = db.scalar(select(User).where(User.id == user_id))

    if not isinstance(role, UserRole):
        return "invalid_role"

    if user is None:
        return "user_not_found"

    if user.id == admin.id:
        return "cannot_change_own_role"
    
    if user.role == UserRole.ADMIN and role != UserRole.ADMIN:
        admin_count = db.scalar(
            select(func.count(User.id))
            .where(User.role == UserRole.ADMIN)
            .where(User.is_active.is_(True))
        )

        if admin_count <=1:
            return "last_admin"

    user.role = role

    try:
        db.commit()
        db.refresh(user)
    except Exception:
        db.rollback()
        raise

    return user