import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongo:27017")

client = AsyncIOMotorClient(MONGO_URL)
db = client["library"]

# Колекції
books_collection = db["books"]
users_collection = db["users"] # Нова колекція для користувачів