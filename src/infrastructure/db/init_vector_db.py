from infrastructure.db.init_mongo import get_mongo_client
import os



def get_mongo_collection():
    client = get_mongo_client()
    dbName = os.getenv("MONGO_VS_DB_NAME")
    print(f"Getting client {client} from {dbName}")
    collectionName = os.getenv("MONGO_VS_COLLECTION_NAME")
    print(f"Getting collection {collectionName} from {dbName}")
    collection = client[dbName][collectionName]
    return collection