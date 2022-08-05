import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

def get_secret(secret_name, kv_uri):

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=kv_uri, credential=credential)

    print(f"Retrieving your secret from {kv_uri}.")

    retrieved_secret = client.get_secret(secret_name)

    print(f"Your secret is '{retrieved_secret.value}'.")

    return retrieved_secret.value