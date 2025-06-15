from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb+srv://<db_username>:<db_password>@cluster0.uvbf5of.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = None
db = None

async def connect_to_mongo():
    global client, db
    client = AsyncIOMotorClient(MONGO_DETAILS)
    db = client.voice_assistant
