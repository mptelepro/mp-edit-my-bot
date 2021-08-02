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

@Jebot.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    update_channel = "@bigmoviesworld"
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("🤭 Sorry Dude, You are B A N N E D 🤣🤣🤣")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="𝐘𝐨𝐮 𝐦𝐮𝐬𝐭 𝐣𝐨𝐢𝐧 𝐨𝐮𝐫 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 ᴛᴏ ᴜꜱᴇ ᴍᴇ </b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" 🔰JOIN OUR CHANNEL🔰 ", url=f"https://t.me/bigmoviesworld")]
              ])
            )
            return
        except Exception:
            await update.reply_text("Something Wrong. Contact my Support Group")
            return 
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'Developers', url="https://t.me/CrazyBotsz"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('Developers', url='https://t.me/CrazyBotsz'),
        InlineKeyboardButton('Source Code 🧾', url ='https://github.com/CrazyBotsz/Adv-Auto-Filter-Bot-V2')
    ],[
        InlineKeyboardButton('Support 🛠', url='https://t.me/CrazyBotszGrp')
    ],[
        InlineKeyboardButton('Help ⚙', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

@Jebot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>



~ @mpazaan</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "😈Back😈", callback_data="start"),
                                        InlineKeyboardButton(
                                            "😆Group😀", callback_data="about"),                               
                                        InlineKeyboardButton(
                                            "😈About😈", callback_data="bots"),
                                  ],[
                                        InlineKeyboardButton(
                                            "😆Bots😆", callback_data="mp"),
                                        InlineKeyboardButton(
                                            "😆Channel😆", callback_data="channel"),
                                        InlineKeyboardButton(
                                            "😆Admins😆", callback_data="admins"),               
                                 ],[
                                        InlineKeyboardButton(
                                            "🤖Source Code🤖", url="https://t.me/munnipopz")
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
