import imghdr, os
from asyncio import gather
from traceback import format_exc
from pyrogram import filters, Client
from pyrogram.types import *
from pyrogram.errors import *
# from utils.files import *
# from utils.stickerset import *
    


# © BugHunterCodeLabs ™
# © bughunter0
# 2021
# Copyright - https://en.m.wikipedia.org/wiki/Fair_use

import os , glob
from os import error
import logging
import pyrogram
import time
import math
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message, Sticker, Document


bughunter0 = Client(
    "Sticker-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

MAX_STICKERS = (120)  # would be better if we could fetch this limit directly from telegram
SUPPORTED_TYPES = ["jpeg", "png", "webp", "gif", "mp4"]
    

START_STRING = """ Hi {}, I'm Sticker Bot. 

I can Provide all Kind of Sticker Options Here """


JOIN_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('↗ Join Here ↗', url='https://t.me/nasrani_update')
        ]]
    )

DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")


@Client.on_message(filters.chat(-1001203428484) & filters.command('start_sticker'))
async def start_sticker(bot, update):
    text = START_STRING.format(update.from_user.mention)
    reply_markup = JOIN_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )


@Client.on_message(filters.chat(-1001203428484) & filters.command('ping'))
async def ping(bot, message):
    start_t = time.time()
    rm = await message.reply_text("Checking")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")



@Client.on_message(filters.chat(-1001203428484) & filters.command('alive'))
async def ping(bot, message):
    await message.reply_document(f"BQACAgQAAx0CbSitBQACETJkw9__TNjSs50hmpGPXnxovk6eTAACJw4AAltmEFFvEc8DS7Kipx4E")
    




@Client.on_message(filters.chat(-1001203428484) & filters.command('getsticker'))
async def getstickerasfile(bot, message):      
    try :     
                     
        tx = await message.reply_text("Downloading...")
        file_path = DOWNLOAD_LOCATION + f"{message.chat.id}.WEBM"
        await message.reply_to_message.download(file_path)   
        await tx.edit("Downloaded")
        await tx.edit("Uploading...")
        start = time.time()
        await message.reply_document(file_path,caption="©NASRANI_UPDATE")
        await tx.delete()   
        os.remove(file_path)
    except Exception as error:
        print(error)    





@Client.on_message(filters.chat(-1001203428484) & filters.command('clearcache'))
async def clearcache(bot, message):   
    # Found some Files showing error while Uploading, So a method to Remove it !!  
    txt = await message.reply_text("Checking Cache")
    await txt.edit("Clearing cache")
    dir = DOWNLOAD_LOCATION
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist :
           i =1
           os.remove(f)
           i=i+1
    await txt.edit("Cleared "+ str(i) + "File") 
    await txt.delete()
    

@Client.on_message(filters.chat(-1001203428484) & filters.command('stickerid'))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply_text(
#       chat_id=message.chat.id,
       text=f"**Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("Oops !! Not a sticker file")



@Client.on_message(filters.chat(-1001203428484) & filters.command('find'))
async def find(bot, message):  
    txt = await message.reply_text("Validating Sticker ID")
    stickerid = message.reply_to_message.text
    chat_id = message.chat.id
    await txt.delete()
    await bot.send_sticker(chat_id,f"{stickerid}")
   



@Client.on_message(filters.chat(-1001203428484) & filters.command('doc'))
async def document(bot, message):  
    documentid= message.reply_to_message.text
    chat_id = message.chat.id
#    await txt.delete()
    m = await message.reply_text("**♻ 𝙲𝚘𝚗𝚟𝚎𝚛𝚝 𝚈𝚘𝚞𝚛 𝙵𝚒𝚕𝚎. ♻**......\n\n[░░░░░░░░░░] 00%")
#    await m.edit("**♻ 𝙲𝚘𝚗𝚟𝚎𝚛𝚝  𝙵𝚒𝚕𝚎... ♻**......\n\n[▇▇░░░░░░░░] 20%")
#    await m.edit("**♻ 𝙲𝚘𝚗𝚟𝚎𝚛𝚝  𝙵𝚒𝚕𝚎... ♻**......\n\n[▇▇▇▇░░░░░░] 40%")
#    await m.edit("**♻ 𝙲𝚘𝚗𝚟𝚎𝚛𝚝  𝙵𝚒𝚕𝚎... ♻**......\n\n[▇▇▇▇▇░░░░░] 50%")
#    await m.edit("**♻ 𝙲𝚘𝚗𝚟𝚎𝚛𝚝  𝙵𝚒𝚕𝚎... ♻**......\n\n[▇▇▇▇▇▇▇░░░] 70%")
#    await m.edit("**♻ 𝙲𝚘𝚗𝚟𝚎𝚛𝚝  𝙵𝚒𝚕𝚎... ♻**......\n\n[▇▇▇▇▇▇▇▇░░] 80%")
#    await m.edit("**♻ 𝙲𝚘𝚗𝚟𝚎𝚛𝚝  𝙵𝚒𝚕𝚎... ♻**......\n\n[▇▇▇▇▇▇▇▇▇▇] 100%")
#    await m.edit("📤Uploading....")
    await m.edit("📤Uploading.....")
    k = await bot.send_document(chat_id,f"{documentid}")
    await asyncio.sleep(120)
    await k.delete()



@Client.on_message(filters.chat(-1001203428484) & filters.command('file'))
async def documentid(bot, message):   
    if message.reply_to_message.document:
       await message.reply_text(
#       chat_id=message.chat.id,
       text=f"**Sticker ID is**  \n `{message.reply_to_message.document.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.document.file_unique_id}`", quote=True)
    else: 
       await message.reply("Oops !! Not a sticker file")







@Client.on_message(filters.chat(-1001203428484) & filters.command('findsticker'))
async def findsticker(bot, message):  
    try:
        
        txt = await message.reply_text("Validating Sticker ID")
        stickerid = str(message.reply_to_message.text)
        chat_id = str(message.chat.id)
        await txt.delete()
        await bot.send_sticker(chat_id,f"{stickerid}")
     
    except Exception as error:
        print(error)
        txt = await message.reply_text("Not a Valid File ID")

      






@Client.on_message(filters.chat(-1001203428484) & filters.command('get_sticker'))
async def sticker_image(_, message: Message):
    r = message.reply_to_message

    if not r:
        return await message.reply("Reply to a sticker.")

    if not r.sticker:
        return await message.reply("Reply to a sticker.")

    m = await message.reply("Sending..")
    f = await r.download(f"{r.sticker.file_unique_id}.png")
    k = await message.reply_photo(f)
    s = await message.reply_document(f)
    

    await m.delete()
    os.remove(f)
