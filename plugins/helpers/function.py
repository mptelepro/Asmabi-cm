from asyncio import gather
from datetime import datetime, timedelta
from io import BytesIO
from math import atan2, cos, radians, sin, sqrt
from os import execvp
from random import randint
from re import findall
from re import sub as re_sub
from sys import executable
from aiohttp import ClientSession
from info import PICS
import aiofiles
import speedtest
from PIL import Image
from pyrogram.types import Message

from pyrogram import filters, Client
from pyrogram.types import Message
from requests import get
import os
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



aiohttpsession = ClientSession()

async def make_carbon(code, message):
    text = message.text.split(None, 1)[1]
    url = get(f"https://api.single-developers.software/logo?name={text}").history[1].url
    async with aiohttpsession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image
