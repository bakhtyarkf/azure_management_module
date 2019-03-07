import getpass
import sys
sys.path.append("..")

import config

def get_graph_creds():
    username = input("Enter your Azure User Name : ")
    password = getpass.getpass("Enter your Azure Password : ")
    return {
        "username": username,
        "password": password
    }