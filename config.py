import logging

from telethon import TelegramClient
from telethon.sessions import MemorySession

from os import getenv
from RAUSHAN.data import ALTRON


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = getenv("API_ID", "21803165")
API_HASH = getenv("API_HASH", "05e5e695feb30e25bef47484cc006da7")
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "cb2147ff-d743-49fc-a18e-6a40aec75e77")

BOT_TOKEN = getenv("BOT_TOKEN", default=None)
BOT_TOKEN2 = getenv("BOT_TOKEN2", default=None)
BOT_TOKEN3 = getenv("BOT_TOKEN3", default=None)
BOT_TOKEN4 = getenv("BOT_TOKEN4", default=None)
BOT_TOKEN5 = getenv("BOT_TOKEN5", default=None)
BOT_TOKEN6 = getenv("BOT_TOKEN6", default=None)
BOT_TOKEN7 = getenv("BOT_TOKEN7", default=None)
BOT_TOKEN8 = getenv("BOT_TOKEN8", default=None)
BOT_TOKEN9 = getenv("BOT_TOKEN9", default=None)
BOT_TOKEN10 = getenv("BOT_TOKEN10", default=None)

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="7403621976").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="7403621976"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient(MemorySession(), API_ID, API_HASH)
if BOT_TOKEN:
    X1.start(bot_token=BOT_TOKEN)

X2 = TelegramClient(MemorySession(), API_ID, API_HASH)
if BOT_TOKEN2:
    X2.start(bot_token=BOT_TOKEN2)

X3 = TelegramClient(MemorySession(), API_ID, API_HASH)
if BOT_TOKEN3:
    X3.start(bot_token=BOT_TOKEN3)

X4 = TelegramClient(MemorySession(), API_ID, API_HASH)
if BOT_TOKEN4:
    X4.start(bot_token=BOT_TOKEN4)

X5 = TelegramClient(MemorySession(), API_ID, API_HASH)
if BOT_TOKEN5:
    X5.start(bot_token=BOT_TOKEN5)

X6 = TelegramClient(MemorySession(), API_ID, API_HASH)
if BOT_TOKEN6:
    X6.start(bot_token=BOT_TOKEN6)

X7 = TelegramClient(MemorySession(), API_ID, API_HASH)
if BOT_TOKEN7:
    X7.start(bot_token=BOT_TOKEN7)

X8 = TelegramClient(MemorySession(), API_ID, API_HASH)
if BOT_TOKEN8:
    X8.start(bot_token=BOT_TOKEN8)

X9 = TelegramClient(MemorySession(), API_ID, API_HASH)
if BOT_TOKEN9:
    X9.start(bot_token=BOT_TOKEN9)

X10 = TelegramClient(MemorySession(), API_ID, API_HASH)
if BOT_TOKEN10:
    X10.start(bot_token=BOT_TOKEN10)
