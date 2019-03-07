from azure.graphrbac import GraphRbacManagementClient
from azure.common.credentials import UserPassCredentials
from azure.graphrbac.models import UserCreateParameters, PasswordProfile
import adal
import sys
sys.path.append("..")

from config import config

def connect_to_graphapi(user_name, password):
    
    credentials = UserPassCredentials(user_name, password, resource="https://graph.windows.net")
    graph_client = GraphRbacManagementClient(credentials, config.TENANT)
    return graph_client


def adal_auth_header():
    auth_context = adal.AuthenticationContext(config.AUTHORITY_URL)
    token_response = auth_context.acquire_token_with_client_credentials(config.RESOURCE_URL, config.CLIENT_ID, config.CLIENT_SECRET)
    return {'Authorization': 'Bearer ' + token_response['accessToken'],
            'Accept': 'application/json',
            'Content-Type': 'application/json'}