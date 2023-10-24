import asyncio
import pyrogram
from pyrogram import Client, filters
from YukkiMusic import settingsApp
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from config import LOG, LOG_GROUP_ID
from YukkiMusic import app
from YukkiMusic.utils.database import is_on_off
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME
from YukkiMusic.misc import SUDOERS
import re
import sys
import os
import random
from time import time
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters




load_dotenv()




def get_file_id(msg: Message):

    if msg.media:

        for message_type in (

            "photo",

            "animation",

            "audio",

            "document",

            "video",

            "video_note",

            "voice",

            # "contact",

            # "dice",

            # "poll",

            # "location",

            # "venue",

            "sticker",

        ):

            obj = getattr(msg, message_type)

            if obj:

                setattr(obj, "message_type", message_type)

                return obj







#@app.on_message(command([""]) & filters.group &
#async def khalid(client: Client, message: Message):
    #usr = await client.get_users(message.from_user.id)
    #name = usr.first_name
    #async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    #await message.reply_photo(photo.file_id,       caption=f"""ᴜsᴇʀ -› {message.from_user.mention}\n𝘂𝘀𝗲𝗿𝗻𝗮𝗺𝗲 -› @{message.from_user.username}\nɪᴅ -› {message.from_user.id}\nbio » {bio}""", 
        #reply_markup=InlineKeyboardMarkup(

            #[

                #[

                    #InlineKeyboardButton(

                        #name, url=f"https://t.me/{message.from_user.id}")

                #],

            #]

        #),

    #)

@app.on_message(filters.regex("^$") & filters.group & SUDOERS)
async def khalid(client: Client, message: Message):

    usr = await client.get_chat(message.from_user.id)

    name = usr.first_name

    bio = usr.bio




    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):

                    await message.reply_photo(photo.file_id,       caption=f"""• In the end, you are the bad, and they are the innocent\n\n• 𝑵𝒂𝒎𝒆 -› {message.from_user.mention}\n• 𝑼𝒔𝒆𝒓 -› @{message.from_user.username}\n• 𝑺𝒕𝒂𝒕𝒔 -› Developer soha\n• 𝑩𝒊𝒐 -› {bio}""", 

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        name, user_id=6228635168)

                ],

            ]

        ),

    )

@app.on_message(filters.regex("^اليسع$") & filters.group & SUDOERS)
async def khalid(client: Client, message: Message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    bio = usr.bio
    await message.reply_video(
        video=f"https://graph.org/file/76fa0ba09eccfbeabd9ba.jpg",
        caption=f"""• In the end, you are the bad, and they are the innocent\n\n• 𝑵𝒂𝒎𝒆 -› {message.from_user.mention}\n• 𝑼𝒔𝒆𝒓 -› @{message.from_user.username}\n• 𝑺𝒕𝒂𝒕𝒔 -› Developer Mira\n• 𝑩𝒊𝒐 -› {bio}""",
        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        name, user_id=6228635168)

                ],

            ]

        ),

    )

@app.on_message(filters.command("ايدي المجموعة", ["", "."]) & ~filters.edited)
async def mira(client: Client, message: Message):
    m_reply = await message.reply_text(f"ID chat** [`{message.chat.id}`]")
    await m_reply_text("")


#السورس - المطور


@app.on_message(filters.regex("^السورس$") & filters.group & ~filters.edited)
async def sourc(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/61dd842dd42e87cef8091.jpg",
        caption=f"""✧ 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑻𝒐 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 ♪\n\n• ᴅᴇᴠᴇʟᴏᴘᴇʀ -› @ASAKIOP\n• ᴄʜᴀɴɴᴇʟ soha -› @Mlze1bot\n\n**-  للاستفسار تواصل مع مطور السورس**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "مطور السورس", user_id=6228635168)
                ],[
                    InlineKeyboardButton(
                       "تحديثات سهى", url=f"https://t.me/Mlze1bot")
                
                 ],

            ]

        ),

    )


@app.on_message(filters.regex("^مطور$") & filters.group & ~filters.edited)
async def aboutd5ev(client: Client, message: Message):
    usr = await client.get_chat(6228635168)
    name = usr.first_name
    bio = (await client.get_chat(6228635168)).bio
    async for photo in client.iter_profile_photos(6228635168, limit=1):
                    await message.reply_photo(photo.file_id, caption=f"""- 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 𝑻𝒐 𝑩𝒐𝒕 𝒔𝒐𝒉𝒂 ♪ -› @ASAKIOP\n\n- 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓'𝒔 𝑩𝒊𝒐 -› {bio}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, user_id=6228635168)
                ],
            ]
        ),
    )

