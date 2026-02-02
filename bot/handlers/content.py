from pyrogram import filters
from pyrogram.types import Message
from bot import app

@app.on_message(filters.text & filters.private)
async def text_handler(_, message: Message):
    await message.reply_text("📽️ Message received")
