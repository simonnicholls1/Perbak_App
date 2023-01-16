from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient
from perbak_api.config import settings


class SecretsService():

    def __init__(self):
        # Create a secret client using the default Azure credentials
        credential = ClientSecretCredential(client_id=settings.client_id,
                                            tenant_id=settings.tenant_id,
                                            client_secret=settings.client_secret)
        self.client = SecretClient(vault_url=settings.vault_url, credential=credential)

    def get_database_credentials(self):
        user = self.client.get_secret("postgres-user")
        password = self.client.get_secret("postgres-password")
        host = self.client.get_secret("postgres-host")
        port = self.client.get_secret("postgres-port")
        name = self.client.get_secret("postgres-db-name")
        return user.value, password.value, host.value, port.value, name.value