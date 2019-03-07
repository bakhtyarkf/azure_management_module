from azure.graphrbac.models import UserCreateParameters, PasswordProfile
from azure.graphrbac import GraphRbacManagementClient
from azure.common.credentials import UserPassCredentials
import json

import sys
sys.path.append("..")

from azure_code.azure_connect.main import connect_to_graphapi
from azure_code.get_creds.main import get_graph_creds

creds = get_graph_creds()

graph_client = connect_to_graphapi(creds['username'], creds['password'])

# def create_user()
#     user = graph_client.users.create(
#         UserCreateParameters(
#             user_principal_name="testbuddy@{}".format(MY_AD_DOMAIN),
#             account_enabled=False,
#             display_name='',
#             mail_nickname='',
#             password_profile=PasswordProfile(
#                 password='',
#                 force_change_password_next_login=True
#             )
#         )
#     )
#     return user


for user in graph_client.users.list():
    print(user)

# graph_½client.users.delete(user.object_id)