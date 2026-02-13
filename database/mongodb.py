import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
if not MONGO_URL:
    raise ValueError("MONGO_URL is not set in .env file")


# Connection settings
MAX_POOL_SIZE = int(os.getenv("MONGO_MAX_POOL_SIZE", 100))

# Create client
client = AsyncIOMotorClient(
    MONGO_URL,
    maxPoolSize=MAX_POOL_SIZE,
    serverSelectionTimeoutMS=5000
)

# Database reference
db = client["hospital_mongo_db"]

# Collection reference
medical_records_collection = db["medical_records"]


async def check_mongo_connection():
    try:
        await client.admin.command("ping")
        return "MongoDB Connected Successfully"
    except Exception as e:
        return f"MongoDB Connection Failed: {str(e)}"
