import os
from pyrogram import Client, filters, enums
from pyrogram.types import Message, User

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = 5891777
API_HASH = '64fa91f5fafd43a3b9dc504f0e2a4d70'

bot = Client(
        "hide",
        bot_token=BOT_TOKEN,
	api_hash=API_HASH,
        api_id=API_ID
    )


@Client.on_message(filters.new_chat_members)
async def welcome(bot, message):
    await message.delete()
    try:
	await message.reply.text(
        text=(f"okda")
	
@Client.on_message(filters.left_chat_member)
async def goodbye(bot, message):
    await message.delete()
    try:
	
        await message.reply.text(
        text=(f"okda")
