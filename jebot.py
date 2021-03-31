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
async def start(_, message):
    bot_uptime = int(time.time() - bot_start_time)
    await message.reply_text(
        f"Already Online Since {formatter.get_readable_time((bot_uptime))},"
        " Maybe Try /help")


@Jebot.on_message(filters.command("help"))
async def help_command(_, message):
    if message.chat.type != "private":
        if len(message.command) >= 2 and message.command[1] == "help":
            text, keyboard = await help_parser(message)
            await message.reply(
                text, reply_markup=keyboard, disable_web_page_preview=True
            )
            return
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Help",
                        url="t.me/" + botinfo.BOT_USERNAME + "?start=help",
                    )
                ]
            ]
        )
        await message.reply("Contact me in PM.", reply_markup=keyboard)
        return
    text, keyboard = await help_parser(message)
    await message.reply_photo(
        caption=text,
        photo="https://hamker.me/z/b8vzvds.png",
        reply_markup=keyboard)

@Jebot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Telegraph Bot Help!

Just send a photo or video less than 5mb file size, I'll upload it to telegraph.

~ @Infinity_BOTs</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="start"),
                                        InlineKeyboardButton(
                                            "About", callback_data="about"),
                                        InlineKeyboardButton(
                                            "About", callback_data="mp"),
                                        InlineKeyboardButton(
                                            "Bots", callback_data="bots"),
                                  ],[
                                        InlineKeyboardButton(
                                            "Source Code", url="https://t.me/munnipopz")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("mp"))
async def mp(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Mp Telegraph Bot!</b>


<b>~ @munnipopz</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="help"),
                                        InlineKeyboardButton(
                                            "About", callback_data="about")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b></b>

<b>~ </b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Start", callback_data="start")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("bots"))
async def bots(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Bots Telegraph Bot!</b>

<b>♞ Developer:</b> <a href="https://t.me/munnipopz</a>

<b>♞ Support:</b> <a href="https://t.me/munnipopz">Infinity BOTs Support</a>

<b>♞ Library:</b> <a href="https://t.me/munnipopz">Pyrogram</a>

<b>~ @munnipopz</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Source Code", url="https://t.me/munnipopz")
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
      elif "mp" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "bots" in cb_data:
        await update.message.delete()
        await bots(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)

print(
    """
Bot Started!
Join @munnipopz
"""
)

Jebot.run()
