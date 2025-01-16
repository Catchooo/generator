import secrets
import string

def generate_password(length=12):
    
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


password_length = int(input("Скільки символів має код?: "))


generated_password = generate_password(password_length)
print("Згенерований пароль::", generated_password)
