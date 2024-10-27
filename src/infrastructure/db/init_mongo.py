from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from infrastructure.db.models.document import DocumentModel
from beanie import init_beanie
import dotenv
import os

dotenv.load_dotenv()


def get_mongo_client_with_motor():
    mongo_url = os.getenv("MONGO_URL")
    return AsyncIOMotorClient(mongo_url)

def get_mongo_client():
    mongo_url = os.getenv("MONGO_URL")
    return MongoClient(mongo_url)

async def init_mongo(client):
    await init_beanie(database=client["botcito"], document_models=[DocumentModel])
    print("MongoDB initialized")


