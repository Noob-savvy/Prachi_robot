from motor.motor_asyncio import AsyncIOMotorClient 
from pymongo import MongoClient
from pyrogram import Client

import config

from ..logging import LOGGER

TEMP_MONGODB = ""


if config.MONGO_DB_URI is None:
    LOGGER(__name__).warning("No MONGO DB URL found.")
    temp_client = Client(
        "Savvy",
        bot_token=config.BOT_TOKEN,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
    )
    temp_client.start()
    info = temp_client.get_me()
    username = info.username
    temp_client.stop()
    _mongo_async_ = _mongo_client_(TEMP_MONGODB)
    _mongo_sync_ = MongoClient(TEMP_MONGODB)
    mongodb = _mongo_async_[username]
    pymongodb = _mongo_sync_[username]
else:
    _mongo_async_ = AsyncIOMotorClient(config.MONGO_DB_URI)
    _mongo_sync_ = MongoClient(config.MONGO_DB_URI)
    mongodb = _mongo_async_.Savvy
    pymongodb = _mongo_sync_.Savvy

## Database For Broadcast subscription by Savvy music

MONGODB_CLI = MongoClient(config.MONGO_DB_URI)
db = MONGODB_CLI["subscriptions"]
