from Security.PasswordHasher import *

hashed = hash_password("Capri123")

print(verify_password("Capri123", hashed))
print(verify_password("WrongPassword", hashed))