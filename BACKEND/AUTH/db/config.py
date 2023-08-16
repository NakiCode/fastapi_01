import motor.motor_asyncio
from dotenv_config import Config

config = Config('.env')
DB_URL = config('DB_URL')
DB_NAME = config('DB_NAME')

client = motor.motor_asyncio.AsyncIOMotorClient(DB_URL)
database = client.DB_NAME
