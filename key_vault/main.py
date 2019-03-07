from azure.keyvault import KeyVaultClient, KeyVaultAuthentication
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.keyvault import KeyVaultManagementClient

import sys
sys.path.append("..")

from config import config

def get_key_from_vault(VAULT_URL, SECRET_ID, SECRET_VERSION):
    def auth_callback(server, resource, scope):
        credentials = ServicePrincipalCredentials(
            client_id = config.CLIENT_ID,
            secret = config.CLIENT_SECRET,
            tenant = config.TENANT,
            resource = "https://vault.azure.net"
        )
        token = credentials.token
        return token['token_type'], token['access_token']

    kv_client = KeyVaultClient(KeyVaultAuthentication(auth_callback))
    secret_bundle = kv_client.get_secret(VAULT_URL, SECRET_ID, SECRET_VERSION)
    return secret_bundle.value


def create_key_in_vault(GROUP_NAME, KV_NAME):
    kvm_clieent = KeyVaultManagementClient(credentials, subscription_id)
    operation = kvm_clieent.vaults.create_or_update(
        GROUP_NAME,
        KV_NAME,
        {
            'location': 'westeurope',
            'properties': {
                'sku': {
                    'name': 'standard'
                },
                'tenant_id': config.TENANT_ID,
                'access_policies': [{
                    'tenant_id': config.TENANT_ID,
                    'object_id': config.USER_OBJECT_ID,
                    'permissions': {
                        'keys': ['all'],
                        'secrets': ['all']
                    }
                }]
            }
        }
    )

    vault = operation.result()

    return {
        VAULT_URI:  vault.properties.vault_uri,
    }