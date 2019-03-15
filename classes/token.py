# Will handle login tokens
import random
import time
import os

max_time = 1000
length = 128
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+="

def token_file(user_name):
    return "storage/users/"+user_name+"/tokens/"

def reap_tokens():
    for user in os.listdir("storage/users/"):
        for token in os.listdir(token_file(user)):
            with open(token,"r") as f:
                age = int(f.read())
            if age + max_time < time.time():
                os.remove(token)

def gen_token(user_name):
    # Make Token string
    token = ""
    for i in range(length):
        token += random.choice(charset)
    # Write Token File
    with open(token_file(user_name)+token,"w") as f:
        f.write(str(int(time.time())))
    
    return token

def check_token(user_name,token):
    # Check if token exsists
    if token not in os.listdir(token_file(user_name)):
        return False
    
    with open(token_file(user_name)+token,"r") as f:
        time_made = int(f.read())

    if time_made > time.time() - max_time:
        with open(token_file(user_name)+token,"w") as f:
            f.write(str(int(time.time())))
        return True
    else:
        os.remove(token_file(user_name)+token)
        return False