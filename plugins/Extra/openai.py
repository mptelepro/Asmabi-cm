from pyrogram import Client, filters
from plugins.helpers.engine import ask_ai
# from info import SUPPORT_CHAT
support = "https://t.me/NASRANI_SUPPORT"



# @Client.on_message(filters.chat(-1001203428484) & filters.text & filters.command('openai'))
# async def openai_ask(client, message):

#    if len(message.command) == 1:
#       return await message.reply_text("Give an input!")
#    m = await message.reply_text("👀")
#    await ask_ai(client, m, message)
   


@Client.on_message(filters.chat(-1001203428484) & filters.text & filters.command('openai'))
async def openai_ask(client, message):
    chat_type = message.chat.type
    if chat_type == enums.ChatType.PRIVATE:
        return await message.reply_text("This Command Work Only in group\n\nTry it in your own group")
    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        grpid = message.chat.id
        title = message.chat.title
    else:
        return
    userid = message.from_user.id
    user = await bot.get_chat_member(grpid, userid)
    if user.status != enums.ChatMemberStatus.ADMINISTRATOR and user.status != enums.ChatMemberStatus.OWNER and str(userid) not in ADMINS:
        return
    else:
        pass
    if len(message.command) == 1:
        return await message.reply("<b>Give me a tutorial link along with this command\n\nCommand Usage: /set_tutorial your tutorial link</b>")
    elif len(message.command) == 2:
    
#       return await message.reply_text("Give an input!")
        m = await message.reply_text("👀")
        await ask_ai(client, m, message)

    


