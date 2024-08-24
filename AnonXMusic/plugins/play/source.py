import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from RaGaBMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(filters.command(["سورس","السورس","ليثون"], ""))
async def source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/3d8ed08f63990ae689bd1.jpg",
        caption=f"• 𝗧𝗵𝗲 𝗕𝗲𝘀𝘁 𝗦𝗼𝘂𝗿𝗰𝗲 𝗢𝗻 𝗧𝗲𝗹𝗲𝗴𝗮𝗺 🎸 .",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
               "𓏺 𝖺𝖣𝖣 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗉𝗌 .", url=f"https://t.me/{client.me.username}?startgroup=true"),
                   ],
                   [
                   InlineKeyboardButton(
                   "‹ 𝖲𝗎𝗉𝗉𝗈𝗎𝗋𝗍 ›", url=f"https://t.me/H_8_o"),
                    InlineKeyboardButton(
                        "‹ 𝖲𝗈𝗎𝗋𝖼𝖾 ›", url=f"https://t.me/A1DIIU"),
                   ],
                   [
                    InlineKeyboardButton(
                       "‹ 𝖣𝖾𝗏¹ ›", user_id=7004732448),
                    InlineKeyboardButton(
                        "‹ 𝖣𝖾𝗏² ›", user_id=7004732448),
                   ],
                   [
                   InlineKeyboardButton(
                        "‹ اغلاق ›", callback_data="close"),
               ],
          ]
        ),
    )
