from passlib.context import CryptContext
import json
import os
login_credentials = r'..\Backend\Credentials.json'
user_data = r'..\Backend\User_Info.json'

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds = 20000
)

def encrypt_string(password):
    return (pwd_context.encrypt(password))

def check_encrypted_string(password, hashed):
    return (pwd_context.verify(password, hashed))

def Login_Custom(user_name, pw):
    file = open (login_credentials, 'r', encoding = 'utf-8')
    data = json.load(file)
    file.close()
    key = list((data.keys()))
    count = 0
    for element in key:
        if check_encrypted_string (user_name, element) == True:
            count += 1
            if check_encrypted_string (pw, data[element]) == True:
                state = True
            else:
                state = False
            break
    if count == 0:
        state = 0
    return state

def Register_Custom(new_user, new_pass, name, team, age):
    if (not new_user) or (not new_pass) or (not name) or (not age):
        return False
    else:
        obj = dict()
        obj = {'username' : new_user, 'name' : name, 'team' : team, 'age' : age}

        with open (login_credentials, 'r', encoding = 'utf-8') as file:
            data = json.load(file)
        with open (login_credentials, 'w+', encoding = 'utf-8') as outfile:
            data[encrypt_string(new_user)] = encrypt_string(new_pass)
            json.dump(data, outfile)
        with open (user_data, 'r', encoding = 'utf-8') as file:
            data1 = json.load(file)
        with open (user_data, 'w+', encoding = 'utf-8') as outfile:
            data1.append(obj)
            json.dump(data1, outfile)
        return True

def Username_Check(user_try):
    file = open (login_credentials, 'r', encoding = 'utf-8')
    data = json.load(file)
    file.close()
    key = list((data.keys()))
    for element in key:
        if check_encrypted_string (user_try, element) == True:
            return False
