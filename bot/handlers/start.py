from pyrogram import filters
from pyrogram.types import Message
from bot import app

@app.on_message(filters.command("start") & filters.private)
async def start_handler(_, message: Message):
    await message.reply_text("✅ Bot is alive!")
