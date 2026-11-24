from sqlalchemy.orm import Session
from sqlalchemy import select

from Models.User import User
from DTOs.UserDTO import LogInDTO, RegisterDTO
from Security.PasswordHasher import hash_password, verify_password

def get_user_by_email(email: str, db: Session):
    statement = (select(User).
                 where(User.email == email))

    return db.scalar(statement)

def get_user_by_username(username: str, db: Session):
    statement = (select(User).
                 where(User.username == username))

    return db.scalar(statement)

def register_user(request: RegisterDTO, db: Session):
    email_exists = get_user_by_email(request.email, db)
    username_exists = get_user_by_username(request.username, db)

    if email_exists is not None:
        return "email_exists"
    elif username_exists is not None:
        return "username_exists"
    
    user = User(
        username = request.username,
        email = request.email,
        password_hash = hash_password(request.password)
        )

    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception:
        db.rollback()
        raise
    
    return user

def login_user(request: LogInDTO, db: Session):
    statement = (select(User)
                 .where(User.email == request.email))
    
    user = db.scalar(statement)

    if user is None:
        return None
    elif not user.is_active:
        return None

    password_is_correct = verify_password(request.password, user.password_hash)

    if not password_is_correct:
        return None

    return user