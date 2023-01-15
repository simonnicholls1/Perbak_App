from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


class SecretsService():

    def __init__(self):
        # Create a secret client using the default Azure credentials
        credential = DefaultAzureCredential()
        self.client = SecretClient(vault_url="https://perbak-keys.vault.azure.net", credential=credential)

    def get_database_credentials(self):
        user = self.client.get_secret("postgres_service_user")
        password = self.client.get_secret("postgres_service_password")
        host = self.client.get_secret("postgres_host")
        port = self.client.get_secret("postgres_port")
        name = self.client.get_secret("postgres_db_name")
        return user, password, host, port, name