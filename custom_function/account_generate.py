import random
import string

def generate_username(length=7):
    characters = string.ascii_letters + string.digits
    return "A" + ''.join(random.choice(characters) for _ in range(length))

def generate_groupname(length=7):
    characters = string.ascii_letters
    return "A" + ''.join(random.choice(characters) for _ in range(length))

def generate_password(length=11):
    characters = string.ascii_letters + string.digits + string.punctuation
    return  "A" + ''.join(random.choice(characters) for _ in range(length))

# 回傳一個新的admin
def return_new_admin_info()->(str, str, str):
    return  {"groupname":generate_groupname(), "username":generate_username(), "password":generate_password()}

# 回傳一個新的使用者
def return_new_user_info()->{str, str}:
    return {"username":generate_username(), "password":generate_password()}
