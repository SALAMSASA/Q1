import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from RaGaBMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(filters.command(["مصنع","مصنع سلوم","المصنع","مصنع السورس"], ""))
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/3d8ed08f63990ae689bd1.jpg",
        caption=f"<b>• اهلا بك عزيزي {message.from_user.mention()} اليك مصانع سورس ليثون</b>",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "سورس ليثون", url=f"https://t.me/A1DIIU"),
                   ],
                   [
                    InlineKeyboardButton(
                       "لتنصيب بوت ميوزك", url=f"https://t.me/H_8_o"),
                       
                    InlineKeyboardButton(
                        "لتنصيب بوت حماية", url=f"https://t.me/S_1_02"),                  ],
                  [
                   InlineKeyboardButton(
                        "إغلاق", callback_data="close"),
               ],
          ]
        ),
    )
