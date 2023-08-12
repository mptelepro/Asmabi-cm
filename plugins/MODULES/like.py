### Importing
# Importing External Packages
from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Update,
    Message,
    CallbackQuery
)

# Importing Inbuilt Packages
import logging

# Importing developer defined module
from plugins.helpers.Like import *


### For Displaying Errors&Warnings Better
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
logging.getLogger(
    "pyrogram"
).setLevel(
    logging.WARNING
)


### Global Variable
taskList = []


### Starting Bot
app = Client(
    "ButtonBot",
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)


### Handlers
# Button adder
@Client.on_message(filters.group)
async def buttonAdder(bot:Update, msg:Message):
    return await msg.edit_reply_markup(
        InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👍",
                        callback_data = "👍"
                    ),
                    InlineKeyboardButton(
                        "👎",
                        callback_data = "👎"
                    )
                ]
            ]
        )
    )

# Button Trigger
@Client.on_callback_query()
async def buttonHandler(bot:Update, callback:CallbackQuery):
    task = await ButtonTrigger.create(callback)
    taskList.append(task)
    return
