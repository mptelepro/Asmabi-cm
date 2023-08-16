from pyrogram import Client, filters, enums
from plugins.helpers.engine import ask_ai
from database.users_chats_db import db
# from info import SUPPORT_CHAT
support = "https://t.me/NASRANI_SUPPORT"
chat_id = "-1001203428484"


# @Client.on_message(filters.chat(-1001203428484) & filters.text & filters.command('openai'))
# async def openai_ask(client, message):

#    if len(message.command) == 1:
#       return await message.reply_text("Give an input!")
#    m = await message.reply_text("👀")
#    await ask_ai(client, m, message)
   

@Client.on_message(filters.chat(-1001203428484) & filters.text & filters.command('openai'))
async def openai_ask(client, message):
    if not chat.id:
        m = await message.reply_text("👀")

        if len(message.command) == 1:
            return await message.reply_text("Give an input!")
        m = await message.reply_text("👀")
        await ask_ai(client, m, message)
   
