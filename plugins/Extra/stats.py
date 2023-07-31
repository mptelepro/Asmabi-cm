#Made By @shamil_shaz_1

import os
import math
import time
from info import ADMINS
import heroku3
import requests
from pyrogram import Client, filters, enums
from database.users_chats_db import db
from Script import script
from utils import temp
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto

#=====================================================
BOT_START_TIME = time.time()
CMD = ['.']
# CMD = ['.' '/']
HRK_API = (os.environ.get("HRK_API", "6e8fad06-0644-412b-845d-197db1e08ec9"))
#=====================================================

@Client.on_message(filters.private & filters.user(ADMINS) & filters.command(["dyno"]))        
async def bot_status_cmd(client,message):
    if HRK_API:
        try:
            server = heroku3.from_key(HRK_API)

            user_agent = (
                'Mozilla/5.0 (Linux; Android 10; SM-G975F) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/80.0.3987.149 Mobile Safari/537.36'
            )
            accountid = server.account().id
            headers = {
            'User-Agent': user_agent,
            'Authorization': f'Bearer {HRK_API}',
            'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
            }

            path = "/accounts/" + accountid + "/actions/get-quota"

            request = requests.get("https://api.heroku.com" + path, headers=headers)

            if request.status_code == 200:
                result = request.json()

                total_quota = result['account_quota']
                quota_used = result['quota_used']

                quota_left = total_quota - quota_used
                
                total = math.floor(total_quota/3600)
                used = math.floor(quota_used/3600)
                hours = math.floor(quota_left/3600)
                minutes = math.floor(quota_left/60 % 60)
                days = math.floor(hours/24)

                usedperc = math.floor(quota_used / total_quota * 100)
                leftperc = math.floor(quota_left / total_quota * 100)

#---------text--------🔥

                quota_details = f"""
💫𝐒𝐄𝐑𝐕𝐄𝐑 𝐒𝐓𝐀𝐓𝐔𝐒💫

💠 𝗧𝗼𝗧𝗮𝗹 𝗗𝘆𝗻𝗼 ➪ {total}hr 𝖿𝗋𝖾𝖾 𝖽𝗒𝗇𝗈!
 
💠 𝗗𝘆𝗻𝗼 𝘂𝘀𝗲𝗱 ➪ {used} 𝖧𝗈𝗎𝗋𝗌 ( {usedperc}% )
        
💠 𝗗𝘆𝗻𝗼 𝗿𝗲𝗺𝗮𝗶𝗻𝗶𝗻𝗴 ➪ {hours} 𝖧𝗈𝗎𝗋𝗌 ( {leftperc}% )
        
💠 𝗔𝗽𝗽𝗿𝗼𝘅𝗶𝗺𝗮𝘁𝗲 𝗱𝗮𝘆𝘀 ➪ {days} days left!"""

#----------end---------💯

            else:
                quota_details = ""
        except:
            print("Check your Heroku API key")
            quota_details = ""
    else:
        quota_details = ""

    uptime = time.strftime("%Hh %Mm %Ss", time.gmtime(time.time() - BOT_START_TIME))

    try:
        t, u, f = shutil.disk_usage(".")
        total = humanbytes(t)
        used = humanbytes(u)
        free = humanbytes(f)

        disk = "\n**Disk Details**\n\n" \
            f"> USED  :  {used} / {total}\n" \
            f"> FREE  :  {free}\n\n"
    except:
        disk = ""

    await message.reply_text(
        "<u>💥 𝗖𝘂𝗿𝗿𝗲𝗻𝘁 𝘀𝘁𝗮𝘁𝘂𝘀 𝗼𝗳 𝘆𝗼𝘂𝗿 𝗕𝗼𝘁💥</u>\n\n"
        "💫𝐃𝐁 𝐒𝐓𝐀𝐓𝐔𝐒💫\n"
        f"➪ 𝖡𝗈𝗍 𝖴𝗉𝗍𝗂𝗆𝖾: {uptime}\n"
        f"{quota_details}"
        f"{disk}",
        quote=True,
        parse_mode=enums.ParseMode.MARKDOWN
    )



@Client.on_message(filters.private & filters.user(ADMINS) & filters.command("start", CMD))         
async def ping(bot, message):
    buttons = [[
        InlineKeyboardButton('𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
    ], [                    
        InlineKeyboardButton('𝐔𝐩𝐝𝐚𝐭𝐞', url='https://t.me/bigmoviesworld'),
        InlineKeyboardButton('𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/NasraniChatGroup')
    ], [
        InlineKeyboardButton('𝐃𝐞𝐭𝐚𝐢𝐥𝐬', url='http://telegra.ph/Minnal-murali-03-06-12'),        
        InlineKeyboardButton('𝐇𝐞𝐥𝐩', callback_data='help')          
    ], [
        InlineKeyboardButton('𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩', url='https://t.me/nasrani_update')
    ], [
        InlineKeyboardButton('𝐈𝐧𝐥𝐢𝐧𝐞', switch_inline_query_current_chat=''),
        InlineKeyboardButton('𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬', callback_data=f"setting")
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_document(
        text=script.START_TXT.format(query.from_user.mention, temp.U_NAME, temp.B_NAME),
#        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML
    )
    
