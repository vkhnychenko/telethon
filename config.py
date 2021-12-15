import os
from dotenv import load_dotenv
from loguru import logger
import json

env_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(env_path):
    load_dotenv(dotenv_path=env_path)

logger.add('logs/debug.log', format="{time} {level} {message}", level="ERROR", rotation="1 MB", compression='zip')


API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
SESSION_NAME = f"./sessions/{os.getenv('SESSION_NAME')}"

with open("chats.json", "r") as read_file:
    CHATS = json.load(read_file)

logger.info(CHATS)
