from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from linarobo import OWNER_ID, dispatcher
from linarobo import pbot as client

Mukesh = "https://te.legra.ph/file/5f3b5901d1ccc014dca9c.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Mukesh,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

╔═════ஜ۩۞۩ஜ════╗

 💕𝗠𝗔𝗗𝗘 𝗕𝗬 [THANOS](https://t.me/thanosceo)💕
  
╚═════ஜ۩۞۩ஜ════╝

**[LINA](t.me/{dispatcher.bot.username}) sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•📍ᴏᴡɴᴇʀ📍",f"tg://user?id={OWNER_ID}"
                    ),
                    InlineKeyboardButton(
                        "📍ʀᴇᴘᴏ📍",
                        url="https://t.me/thanos_pro",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "⚡Rᴇᴩᴏ⚡"
_help__ = """
 /repo  ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 
 /source ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ
"""
