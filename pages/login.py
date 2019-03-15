is_page = True
POST = True
GET = False
# This page will handle log in
# it will take the username and password and return a token

import classes


def main(path, args):
    # Loggin in with a password and username
    if "name" in args and "password" in args:

        return 200, {"success":True}
    
    # Loggin in with a `rememberme` token
    elif "name" in args and "token" in args:
        return 200, {"success":True}