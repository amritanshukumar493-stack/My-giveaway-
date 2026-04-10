import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from motor.motor_asyncio import AsyncIOMotorClient

# --- [ CREDENTIALS ] ---
API_ID = 30607967
API_HASH = "c2fd1d5d420922dd0a8eec4e12e7d862"
BOT_TOKEN = "8799938048:AAEnCUuNw5QfFYBCOglT1zZ36IzIyQ6KCBA"
ADMIN_ID = 8074231185
MONGO_URL = "YAHAN_APNA_MONGODB_URL_DALO" # 👈 Very Important

app = Client("losted_cloud", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
db = AsyncIOMotorClient(MONGO_URL)["losted_db"]

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    # (Puraani voting aur UI logic yahan rahega...)
    await message.reply_photo("https://t.me/LostedLSVault/6", caption="🎁 **LOSTED LS VAULT** is Live!")

app.run()
