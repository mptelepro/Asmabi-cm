from pyrogram.types import InputMediaPhoto, InputMediaVideo



@Client.on_message(filters.command("book"))
async def book(bot, message):
    await bot.send_media_group(
        "me",
        [
            InputMediaPhoto("https://telegra.ph/file/442eabcd1bec22e3cca6f.jpg"),
            InputMediaPhoto("https://telegra.ph/file/442eabcd1bec22e3cca6f.jpg", caption="photo caption"),
            InputMediaVideo("https://telegra.ph/file/53e47d78206577914c487.mp4", caption="video caption")
        ]
    )
