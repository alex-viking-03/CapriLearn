from pwdlib import PasswordHash

hasher = PasswordHash.recommended()

def hash_password(password: str):
    return hasher.hash(password)

def verify_password(password: str, password_hash:str):
    return hasher.verify(password, password_hash)