import os
from dotenv import load_dotenv
import json
from loguru import logger

env_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(env_path):
    load_dotenv(dotenv_path=env_path)

logger.add('logs/log.log', format="{time} {level} {message}", level="INFO", rotation="1 MB", compression='zip')


API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
# SESSION_PATH = f"./sessions/{os.getenv('SESSION_NAME')}"
SESSION_NAME = os.getenv('SESSION_NAME')

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
SPREADSHEET_URL = os.getenv("SPREADSHEET_URL")
CREDENTIALS_FILE = os.getenv("CREDENTIALS_FILE", 'data/creds.json')

# with open("chats.json", "r") as read_file:
#     CHATS = json.load(read_file)
#
# logger.info(CHATS)
