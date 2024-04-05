from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 27353035))
API_HASH = getenv("API_HASH", "cf2a75861140ceb746c7796e07cbde9e")
TOKEN = getenv("TOKEN", None)
CHAT = int(getenv("CHAT", "-1005822700831"))
START_PIC = getenv("START_PIC", None)
