is_page = True
POST = True
GET = False
# This page will handle log in
# it will take the username and password and return a token

import classes
import os
import bcrypt


def main(path, args):
    # Loggin in with a password and username
    if "name" in args and "password" in args:
        user_name = args["name"].lower()
        
        # Does user exists
        if user_name in os.listdir("storage/users/"):
            # Get password file
            with open("storage/users/"+user_name+"/password","rb") as f:
                password_hash = f.read()
            success = bcrypt.checkpw(args["password"].encode("utf-8"),password_hash)
            if success:
                return 200, {"sucess":True,"token":classes.token.gen_token(user_name)}
            else:
                return 400, {"success":False,"reason":"Invalid user credentials"}
        else:
            return 400, {"success":False,"reason":"Invalid user credentials"}
    
    # Loggin in with a `remember-me` token
    elif "name" in args and "token" in args:
        return 200, {"success":True}

    else:
        return 400, {"success":False,"reason":"Invalid syntax, name and password/token requierd"}