# (c) @KoshikKumar17
import os
import requests
import pyrogram
import json
from info import LOG_CHANNEL
from pyrogram import Client as Koshik
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('✨ Made By ✨', url='https://t.me/nasrani_update')]])
A = """{} with user id:- {} used /git command."""

@Client.on_message(filters.command(["repo", "repository"]))
async def repo(bot, message):
    if len(message.command) != 2:
        await message.reply_text("/github Username \n\n Like:- `/github hkrrish`", quote=True)
        return
    await message.reply_chat_action(enums.ChatAction.TYPING)
    k = await message.reply_text("**Processing...⏳**", quote=True)    
    un = message.text.split(None, 1)[1]
    await message.reply_text(f'https://github.com/search?q={un}+language%3APython&type=repositories&l=Python&s=updated&o=desc')
    
@Client.on_message(filters.command(["github", "git"]))
async def getgithub(bot, message):
    if len(message.command) != 2:
        await message.reply_text("/github Username \n\n Like:- `/github hkrrish`", quote=True)
        return
    await message.reply_chat_action(enums.ChatAction.TYPING)
    k = await message.reply_text("**Processing...⏳**", quote=True)    
    un = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{un}'
    request = requests.get(URL)
    result = request.json()
    username = result['login']
    url = result['html_url']
    name = result['name']
    company = result['company']
    bio = result['bio']
    created_at = result['created_at']
    avatar_url = result['avatar_url']
    blog = result['blog']
    location = result['location']
    repositories = result['public_repos']
    followers = result['followers']
    following = result['following']
    capy = f"""**Info Of {name}**
**Username:** `{username}`
**Bio:** `{bio}`
**Profile Link:** [Click Here]({url})
**Company:** `{company}`
**Created On:** `{created_at}`
**Repositories:** `{repositories}`
**Blog:** `{blog}`
**Location:** `{location}`
**Followers:** `{followers}`
**Following:** `{following}`

**@kinzanoufal**"""
    await message.reply_photo(photo=avatar_url, caption=capy, reply_markup=BUTTONS)
    await bot.send_message(LOG_CHANNEL, A.format(message.from_user.mention, message.from_user.id)) 
    await k.delete()
        
@Client.on_message(filters.command(["myr", "poory"]))
async def myr(bot, message):
    if len(message.command) != 2:
        await message.reply_text("/github Username \n\n Like:- `/github hkrrish`", quote=True)
        return
    await message.reply_chat_action(enums.ChatAction.TYPING)
    k = await message.reply_text("**Processing...⏳**", quote=True)    
    un = message.text.split(None, 1)[1]
    repositories = requests.get('https://api.github.com/search/repositories')
    data = json.loads(response.text)
    result = request.json()
    title = repo['name']
    url = result['html_url']
    name = result['name']
    company = result['company']
    bio = result['bio']
    created_at = result['created_at']
    avatar_url = result['avatar_url']
    blog = result['blog']
    location = result['location']
    repositories = result['public_repos']
    followers = result['followers']
    following = result['following']
    capy = f"""**Info Of {name}**
**Username:** `{title}`
**Bio:** `{bio}`
**Profile Link:** [Click Here]({url})
**Company:** `{company}`
**Created On:** `{created_at}`
**Repositories:** `{repositories}`
**Blog:** `{blog}`
**Location:** `{location}`
**Followers:** `{followers}`
**Following:** `{following}`

**@kinzanoufal**"""
    await message.reply_text(text=title, reply_markup=BUTTONS)
    await bot.send_message(LOG_CHANNEL, A.format(message.from_user.mention, message.from_user.id)) 
    await k.delete()
     
