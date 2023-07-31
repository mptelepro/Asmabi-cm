import os
from plugins.helpers.vars import ADMINS, DATABASE, DEFAULT_LANGUAGE
from plugins.helpers.admin import Database
from io import BytesIO
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from googletrans import Translator, constants



SETTINGS_TEXT = "Select your language for translating. Current default language is `{}`."

BUTTONS = [InlineKeyboardButton('⚙ Join Updates Channel ⚙', url='https://telegram.me/FayasNoushad')]

db = Katabase(DATABASE)

LANGUAGES = constants.LANGUAGES

LANGUAGES_TEXT = "**Languages**\n"
for language in LANGUAGES:
    LANGUAGES_TEXT += f"\n`{LANGUAGES[language].capitalize()}` -> `{language}`"




@Client.on_message(filters.command(["set"]))
async def settings(bot, update):
    if update.chat.type != enums.ChatType.PRIVATE:
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Click here",
                        url=f"https://telegram.me/{(await bot.get_me()).username}?start=set"
                    )
                ]
            ]
        )
        await update.reply_text(
            text="Set your language via private",
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            quote=True
        )
        return
    if not await db.is_user_exist(update.from_user.id):
        await db.add_user(update.from_user.id)
    await update.reply_text(
        text=SETTINGS_TEXT.format(await db.get_lang(update.from_user.id)),
        disable_web_page_preview=True,
        reply_markup=SETTINGS_BUTTONS,
        quote=True
    )


@Client.on_message(filters.private & filters.command(["unset"]))
async def unset(bot, update):
    if not await db.is_user_exist(update.from_user.id):
        await db.add_user(update.from_user.id)
    await db.update_lang(update.from_user.id, DEFAULT_LANGUAGE)
    await update.reply_text(
        text="Language unset successfully",
        disable_web_page_preview=True,
        quote=True
    )


@Client.on_message(filters.group & filters.command(["tr", "translate"]))
async def command_filter(bot, update):
    if update.reply_to_message:
        if update.reply_to_message.text:
            text = update.reply_to_message.text
        elif update.reply_to_message.caption:
            text = update.reply_to_message.caption
        else:
            return 
    else:
        if update.text:
            text = update.text.split(" ", 1)[1]
        elif update.caption:
            text = update.caption.split(" ", 1)[1]
        else:
            return
    await translate(bot, update, text)





async def translate(update, text):
    await update.reply_chat_action(enums.ChatAction.TYPING)
    message = await update.reply_text("`Translating...`")
    try:
        language = await db.get_lang(update.from_user.id)
    except:
        language = DEFAULT_LANGUAGE
    translator = Translator()
    try:
        translate = translator.translate(text, dest=language)
        translate_text = f"**Translated to {language}**"
        translate_text += f"\n\n`{translate.text}`"
        if len(translate_text) < 4096:
            await message.edit_text(
                text=translate_text,
                disable_web_page_preview=True
            )
        else:
            with BytesIO(str.encode(str(translate_text))) as translate_file:
                translate_file.name = language + ".txt"
                await update.reply_document(
                    document=translate_file
                )
                await message.delete()
                try:
                    os.remove(translate_file)
                except:
                    pass
    except Exception as error:
        print(error)
        await message.edit_text("Something wrong. Contact @TheFayas.")
        return
