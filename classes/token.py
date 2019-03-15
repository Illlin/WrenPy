# Will handle login tokens
import random
import time
import os

max_time = 1000
length = 128
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+="

def token_file(user_name):
    return "storage/users/"+user_name+"/tokens/"

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