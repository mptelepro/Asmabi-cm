from pyrogram import Client, filters
from plugins.helpers.engine import ask_ai
# from info import SUPPORT_CHAT
support = "https://t.me/NASRANI_SUPPORT"



@Client.on_message(filters.chat(-1001203428484) & filters.text & filters.command('openai'))
async def openai_ask(client, message):
    chat_type = message.chat.type
    if chat_type == message.chat.id:
        return await message.reply_text("This Command Work Only in group\n\nTry it in your own group")
#    elif chat_type in -1001203428484:
    if len(message.command) == 1:
       return await message.reply_text("Give an input!")
    m = await message.reply_text("👀")
    await ask_ai(client, m, message)

    


