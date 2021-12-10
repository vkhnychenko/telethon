import os
from dotenv import load_dotenv
from loguru import logger

env_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(env_path):
    load_dotenv(dotenv_path=env_path)

logger.add('logs/debug.log', format="{time} {level} {message}", level="ERROR", rotation="1 MB", compression='zip')

# 58149469 Anton Katin ID
# 233787240 Slavik investor ID
# 309275950 My ID

# -1001188323070 Neutrino
# -1001262886489 Simba
# -642005665 Anton Katin messages
# -657152166 Slavik investor messages
# -652900673 Test chat


API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
SESSION_NAME = os.getenv('SESSION_NAME')
