import logging
import logging.config
from pyrogram import Client
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import Config
#from aiohttp import web
#from pytz import timezone
from datetime import datetime
#from plugins.web_support import web_server
import pyromod

#logging.config.fileConfig('logging.conf')
#logging.getLogger().setLevel(logging.INFO)
#logging.getLogger("pyrogram").setLevel(logging.ERROR)


class Bot(Client):

    def __init__(self):
        super().__init__(
            name="Almighty",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            token=Config.TOKEN,
            workers=200,
            plugins={"root": "HACKSESSIONBOT"},
            sleep_threshold=15,
        )

bot = Bot()
bot.run()
