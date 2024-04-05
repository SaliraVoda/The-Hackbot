import re, os, time

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "") # ⚠️ Required
    TOKEN = os.environ.get("TOKEN", "") # ⚠️ Required
    CHAT = os.environ.get("CHAT", "") # ⚠️ Required
    START_PIC    = os.environ.get("START_PIC", "")  # ⚠️ Required
