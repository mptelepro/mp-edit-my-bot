import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

Jebot = Client(
   "Telegraph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Jebot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await Jebot.send_message(
        chat_id=message.chat.id,
               text="""<b>♞ ᴅᴇᴠᴇʟᴏᴘᴇʀ:</b> <a href="https://dog/t.me/mazhatthullikal</b>

<b>♞ ꜱᴜᴘᴘᴏʀᴛ:</b> <a href="https://dog/t.me/munnipopz</a>

<b>♞ ꜱᴜᴘᴘᴏʀᴛ:</b> <a href="https://dog/t.me/mazhatthullikal">ᴍᴘᴀᴢᴀᴀɴ</a>

<b>♞ ꜱᴜᴘᴘᴏʀᴛ:</b> <a href="https://dog/t.me/mazhatthullikal">ᴘʏʀᴏɢʀᴀᴍ</a>

ʜɪᴛ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ꜰɪɴᴅ ᴏᴜᴛ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴍᴇ</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "🤖ʜᴇʟᴘ🤖", callback_data="help"),
                                        InlineKeyboardButton(
                                            "💓ᴄʜᴀɴɴᴇʟ💓", url="https://t.me/mpazaanbot")
                                    ],[
                                      InlineKeyboardButton(
                                            "👁‍🗨ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ👁‍🗨", url="https://t.me/mazhatthullikal")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "😈ʙᴀᴄᴋ😈", callback_data="start"),
                                        InlineKeyboardButton(
                                            "😆ɢʀᴏᴜᴘ😀", callback_data="about"),                               
                                        InlineKeyboardButton(
                                            "😈ᴀʙᴏᴜᴛ😈", callback_data="bots"),
                                  ],[
                                        InlineKeyboardButton(
                                            "😆ʙᴏᴛꜱ😆", callback_data="mp"),
                                        InlineKeyboardButton(
                                            "😆ᴄʜᴀɴɴᴇʟ😆", callback_data="channel"),
                                        InlineKeyboardButton(
                                            "😆ᴀᴅᴍɪɴꜱ😆", callback_data="admins"),               
                                 ],[
                                        InlineKeyboardButton(
                                            "🤖ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ🤖", url="https://t.me/munnipopz")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("admins"))
async def admins(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>channel</b>

<b>♞ Developer:</b> <a href="https://telegra.ph/file/dd451b9d186d65a2187d5.jpg</a>

<b>♞ Support:</b> <a href="https://dog/t.me/mazhatthullikal">Infinity BOTs Support</a>

<b>♞ Library:</b> <a href="https://telegra.ph/file/dd451b9d186d65a2187d5.jpg">Pyrogram</a>

<b>~ @munnipopz</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "😈Back😈", callback_data="help"),
                                        InlineKeyboardButton(
                                            "😈Source Code😈", url="https://t.me/munnipopz")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("channel"))
async def channel(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>channel</b>

<b>♞ Developer:</b> <a href="https://telegra.ph/file/dd451b9d186d65a2187d5.jpg</a>

<b>♞ Support:</b> <a href="https://dog/t.me/mazhatthullikal">Infinity BOTs Support</a>

<b>♞ Library:</b> <a href="https://telegra.ph/file/dd451b9d186d65a2187d5.jpg">Pyrogram</a>

<b>~ @munnipopz</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "😈Back😈", callback_data="help"),
                                        InlineKeyboardButton(
                                            "😈Source Code😈", url="https://t.me/munnipopz")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("mp"))
async def mp(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Mp</b>

<b>♞ Developer:</b> <a href="https://telegra.ph/file/dd451b9d186d65a2187d5.jpg</a>

<b>♞ Support:</b> <a href="https://dog/t.me/mazhatthullikal">Infinity BOTs Support</a>

<b>♞ Library:</b> <a href="https://telegra.ph/file/dd451b9d186d65a2187d5.jpg">Pyrogram</a>

<b>~ @munnipopz</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "😈Back😈", callback_data="help"),
                                        InlineKeyboardButton(
                                            "😈Source Code😈", url="https://t.me/munnipopz")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Bots</b>

<b>♞ Developer:</b> <a href="https://telegra.ph/file/dd451b9d186d65a2187d5.jpg</a>

<b>♞ Support:</b> <a href="https://dog/t.me/mazhatthullikal">Infinity BOTs Support</a>

<b>♞ Library:</b> <a href="https://telegra.ph/file/dd451b9d186d65a2187d5.jpg">Pyrogram</a>

<b>~ @munnipopz</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "😈Back😈", callback_data="help"),
                                        InlineKeyboardButton(
                                            "😈Source Code😈", url="https://t.me/munnipopz")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("group"))
async def group(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b></b>

<b>~ </b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "😈Back😈", callback_data="help"),
                                        InlineKeyboardButton(
                                            "😈Start😈", callback_data="start")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("bots"))
async def bots(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Bots</b>

<b>♞ Developer:</b> <a href="https://telegra.ph/file/dd451b9d186d65a2187d5.jpg</a>

<b>♞ Support:</b> <a href="https://dog/t.me/mazhatthullikal">Infinity BOTs Support</a>

<b>♞ Library:</b> <a href="https://telegra.ph/file/dd451b9d186d65a2187d5.jpg">Pyrogram</a>

<b>~ @munnipopz</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "😈Back😈", callback_data="help"),
                                        InlineKeyboardButton(
                                            "😈Source Code😈", url="https://t.me/munnipopz")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "group" in cb_data:
        await update.message.delete()
        await group(bot, update.message)
      elif "mp" in cb_data:
        await update.message.delete()
        await mp(bot, update.message)
      elif "bots" in cb_data:
        await update.message.delete()
        await bots(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)
      elif "channel" in cb_data:
        await update.message.delete()
        await channel(bot, update.message)
      elif "admins" in cb_data:
        await update.message.delete()
        await admins(bot, update.message)

print(
    """
Bot Started!
Join @munnipopz
"""
)

Jebot.run()
