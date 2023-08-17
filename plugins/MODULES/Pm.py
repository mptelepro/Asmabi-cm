import os
import logging
from pyrogram import Client, filters, enums
from Script import script
from info import CHANNELS, ADMIN, AUTH_CHANNEL, CUSTOM_FILE_CAPTION, LOG_CHANNEL, ADMINS, PICS
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import random
import asyncio

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@Client.on_message(filters.command("chat") & filters.text)
async def pm_text(client: Client, message):
    content = message.text
    user = message.from_user.first_name
    user_id = message.from_user.id
    lgcd = message.text.split("/chat")
    lg_cd = lgcd[1].lower().replace(" ", "")
    try:   
        if message.from_user.id == ADMIN: 
            await reply_text(client, message)
            return
#        await message.reply_text(
#        text=f"<b>ʜᴇʏ {user} 😍 ,\n\nʏᴏᴜ ᴄᴀɴ'ᴛ ɢᴇᴛ ᴍᴏᴠɪᴇs ꜰʀᴏᴍ ʜᴇʀᴇ. ʀᴇǫᴜᴇsᴛ ɪᴛ ɪɴ ᴏᴜʀ <a href=https://telegram.me/+ps2An00KwZYwNTRl>ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ</a> ᴏʀ ᴄʟɪᴄᴋ ʀᴇǫᴜᴇsᴛ ʜᴇʀᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ 👇</b>",   
#        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 ʀᴇǫᴜᴇsᴛ ʜᴇʀᴇ ", url=f"telegram.me/TeamHMT_Movies")]])
#        )
        info = await client.get_users(user_ids=message.from_user.id)
        reference_id = int(message.chat.id)
        k = await client.send_photo(
            chat_id=int(reference_id),
            photo=f"https://telegra.ph/file/f5a9f3ee907003b1e055e.jpg",
            caption=script.PM_TXT_ATT.format(reference_id, info.first_name, message.from_user.mention),
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('🎁𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬🎁', url="http://t.me/nasrani_bot?startgroup=true")
                            ],
                            [
                                InlineKeyboardButton('📩𝐇𝐞𝐥𝐩📩', callback_data='start'),
                                InlineKeyboardButton('☘𝐀𝐛𝐨𝐮𝐭☘', url="https://t.me/NasraniMovies")
                            ]                            
                        ]
                    )
                )        
	   



	    
        
        await client.send_message(
            chat_id=ADMIN,
            text=script.PM_TXT_ATT.format(reference_id, info.first_name, message.text),
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('🎁𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬🎁', url="http://t.me/nasrani_bot?startgroup=true")
                            ],
                            [
                                InlineKeyboardButton('📩𝐑𝐄𝐐𝐔𝐀𝐒𝐓 𝐆𝐑𝐎𝐔𝐏📩', url="https://t.me/NasraniMovies"),
                                InlineKeyboardButton('☘𝐍𝐄𝐖 𝐌𝐎𝐕𝐈𝐄𝐒☘', url="https://t.me/HDAZmovies")
                            ]                            
                        ]
                    )
                )
        await asyncio.sleep(3000)
        await k.delete()
        
    except Exception as e:
        logger.exception(e)



@Client.on_message(filters.command("share") & filters.private & filters.media)
async def pm_media(client, message):
    if message.from_user.id in ADMINS:
        await replay_media(client, message)
        return
    info = await client.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await client.copy_message(
        chat_id=ADMINS,
        from_chat_id=message.chat.id,
        message_id=message.id,
        caption=script.PM_MED_ATT.format(reference_id, info.first_name),
	parse_mode=enums.ParseMode.HTML
    )

@Client.on_message(filters.command("media") & filters.media)
async def media(client: Client,  message):
	
            photo = message.reply_to_message
            m = await client.copy_message(
                chat_id=ADMIN,
                from_chat_id=message.chat.id,
                message_id=message.id
	    )





@Client.on_message(filters.private & filters.user(ADMIN) & filters.text & filters.command("ok"))
async def reply_textt(client: Client, message):
    try:
        reference_id = True
        if message.reply_to_message is not None:
            file = message.reply_to_message
            try:
                reference_id = file.text.split()[2]
            except Exception:
                pass
            try:
                reference_id = file.caption.split()[2]
            except Exception:
                pass
            await client.send_message(
                text=message.text,
                chat_id=int(reference_id),
#		chat_id=message.reply_to_message.from_user.id,
                parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('🎁𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬🎁', url="http://t.me/nasrani_bot?startgroup=true")
                            ],
                            [
                                InlineKeyboardButton('📩𝐑𝐄𝐐𝐔𝐀𝐒𝐓 𝐆𝐑𝐎𝐔𝐏📩', url="https://t.me/Nasrani_update"),
                                InlineKeyboardButton('☘𝐍𝐄𝐖 𝐌𝐎𝐕𝐈𝐄𝐒☘', url="https://t.me/HDAZmovies")
                            ]                            
                        ]
                    )
                )        
    except Exception as e:
        logger.exception(e)



@Client.on_message(filters.private & filters.media & filters.command("okk"))
async def reply_media(client: Client, message):
    
#    if message.from_user.id in ADMINS:
#        await replay_media(client, message)
#        return
    info = await client.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    try:   
        if message.from_user.id == ADMIN: 
            await reply_textt(client, message)
            return
        k = await client.copy_message(
            chat_id=ADMIN,
            from_chat_id=message.chat.id,
            message_id=message.id)
        m = await client.send_message(
            chat_id=ADMIN,
            text=f"{reference_id} {info.first_name}",
            parse_mode=enums.ParseMode.HTML)
            
        await asyncio.sleep(3000)
        await k.delete()
        
    except Exception as e:
        logger.exception(e)
		



       
        




@Client.on_message(filters.private & filters.user(ADMIN) & filters.media & filters.text & filters.reply)
async def replay_media(client: Client, message):
    try:
        reference_id = True
        if message.reply_to_message is not None:
            file = message.reply_to_message
            try:
                reference_id = file.text.split()[2]
            except Exception:
                pass
            try:
                reference_id = file.caption.split()[2]
            except Exception:
                pass
		    
            await client.copy_message(
                chat_id=int(reference_id),
                from_chat_id=message.chat.id,
                message_id=message.id,
                parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('🎁𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬🎁', url="http://t.me/nasrani_bot?startgroup=true")
                            ],
                            [
                                InlineKeyboardButton('📩𝐑𝐄𝐐𝐔𝐀𝐒𝐓 𝐆𝐑𝐎𝐔𝐏📩', url="https://t.me/NasraniMovies"),
                                InlineKeyboardButton('☘𝐍𝐄𝐖 𝐌𝐎𝐕𝐈𝐄𝐒☘', url="https://t.me/HDAZmovies")
                            ]                            
                        ]
                    )
                )        
    except Exception as e:
        logger.exception(e)
















