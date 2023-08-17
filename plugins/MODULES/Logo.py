import os
from PIL import Image
from pyrogram.types import Message
from pyrogram import Client, filters, enums
from utils import temp


@Client.on_message(filters.command(["pack"]))
async def sticker_image(_, msg: Message):
    replied = msg.reply_to_message
    user_id = msg.from_user.id
    message_id = msg.id
#    name_format = f"StarkBots_{user_id}_{message_id}"
    name_format = f"http://t.me/addstickers/a{user_id}_by_{temp.U_NAME}"
    
    message = await msg.reply("Converting...")
    image = await replied.download(file_name=f"{name_format}.jpg")
    await message.edit("Sending...")
    im = Image.open(image).convert("RGB")
    im.save(f"{name_format}.webp", "webp")
    sticker = f"{name_format}.webp"
    await msg.reply_sticker(sticker)
    await message.delete()
    os.remove(sticker)
    os.remove(image)

    
