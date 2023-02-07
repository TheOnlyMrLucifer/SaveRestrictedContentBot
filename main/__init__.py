#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "3072251"
API_HASH = "23cbf2ffb2404519b1172a7b5394ca13"
BOT_TOKEN = "6187668461:AAF5Zk_geQe97MCO6WZ5KS_9nvnTujW88I8"
SESSION = "BAA9ROpNBqUn0IoSmROUJXD8bwj4ZLQR7BfwcqFrWRWXSHouoLHIGOSUr5twjFfM2HZBWRqJ8g-21bpQU2vrPM0HWAdfHLGFyAmtRDFWpNu6_iYOcgBPTkFG-D8o9kKFxmrUfO5ptvLnznaGT7b-qoJqXjipCw7AYrxmowHusSqtXyfl_snUvBumV0ZIoMMXEoYhuNZcWFYHg9alt3_Yq7tI51be5VdBqRDKiyPLD_DUooGacEC_dWGCOuRGi7EccFCG-fMBH9qc9s66ea0HbICL_owrf_jZTk7BU8mHZuPNYbv3INzMd_GdhlTOfIJtZ-FwYLjj3MkVatQGPikheLQcS8RKoQA"
FORCESUB = "ThePornLeague"
AUTH = "1271155361"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
