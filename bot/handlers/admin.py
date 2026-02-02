from pyrogram import filters
from pyrogram.types import Message
from bot import app
from bot.config import ADMIN_ID

@app.on_message(filters.command("admin") & filters.user(ADMIN_ID))
async def admin_handler(_, message: Message):
    await message.reply_text("👑 Admin OK")
