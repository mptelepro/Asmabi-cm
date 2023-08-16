from pyrogram import Client, filters, enums

import openai
from info import OPENAI, ADMINS, SUPPORT_CHAT, LOG_CHANNEL
async def ai(query):
    
    openai.api_key = OPENAI #Your openai api key
    response = openai.Completion.create(engine="text-davinci-002", prompt=query, max_tokens=100, n=1, stop=None, temperature=0.9, timeout=5)
    return response.choices[0].text.strip()
     
async def ask_ai(client, m, message):
    try:
        message = message.text
        question = message.text.split(" ", 1)[1]
        # Generate response using OpenAI API
        response = await ai(question)
        # Send response back to user
        await m.edit(f" 🕵‍♂ ʀᴇǫᴜꜱᴛᴇᴅ ʙʏ: {message.from_user.mention} \n 🔍 Qᴜᴇʀʏ: {message} \n ʜᴇʀᴇ ɪ ғᴏᴜɴᴅ ғᴏʀ ʏᴏᴜ ǫᴜᴇʀʏ 👇 \n\n <code> {response} </code>")
    except Exception as e:
        # Handle other errors
        error_message = f"An error occurred: {e}"
        await m.edit(error_message)
    



@Client.on_message(filters.group & filters.text & filters.incoming)
async def pm_text(bot, message):
    content = message.text
    user = message.from_user.first_name
    user_id = message.from_user.id
    if content.startswith("/") or content.startswith("#"): return  # ignore commands and hashtags
    if user_id in ADMINS: return # ignore admins
    await message.reply_text("<b>Yᴏᴜʀ ᴍᴇssᴀɢᴇ ʜᴀs ʙᴇᴇɴ sᴇɴᴛ ᴛᴏ ᴍʏ ᴍᴏᴅᴇʀᴀᴛᴏʀs !</b>")
    await bot.send_message(
        chat_id=LOG_CHANNEL,
        text=f"<b>#𝐏𝐌_𝐌𝐒𝐆\n\nNᴀᴍᴇ : {user}\n\nID : {user_id}\n\nMᴇssᴀɢᴇ : {content}</b>"
    )
