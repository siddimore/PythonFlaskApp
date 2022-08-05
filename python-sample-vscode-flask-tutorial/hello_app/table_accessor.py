from azure.data.tables import TableServiceClient
from azure.data.tables import TableClient
import asyncio

# TODO Make this into a class
def create_table_client(connection_string):
    client = TableServiceClient.from_connection_string(conn_str=connection_string)
    return client

# TODO Add method to get entries from a table
def get_single_entity_by_partition_key(connection_string, table_name, parition_key):
    try:
        result=None
        with TableClient.from_connection_string(conn_str=connection_string, table_name=table_name) as table_client:
            filter = f"PartitionKey eq '{parition_key}'"
            print(filter)
            count = 0
            queried_entities = table_client.list_entities()
            # queried_entities = table_client.query_entities(filter)
            for entity in queried_entities:
                count = count + 1
                print(entity)
                result=entity
            print(count)
            print(result)
            return result
    except Exception as ex:
        print(ex)
        pass