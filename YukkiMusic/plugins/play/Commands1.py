import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
import config
from config import BANNED_USERS
from config.config import OWNER_ID
from strings import get_command, get_string
from YukkiMusic import Telegram, YouTube, app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.plugins.play.playlist import del_plist_msg
from YukkiMusic.plugins.sudo.sudoers import sudoers_list
from YukkiMusic.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from YukkiMusic.utils.decorators.language import LanguageStart
from YukkiMusic.utils.inline import (help_pannel, private_panel,
                                     start_pannel)

from YukkiMusic import check_client


@app.on_callback_query(filters.regex("ddd"))
async def dddf(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك !!", show_alert=True)

    await query.edit_message_text(
       f"""\n\n\n╭── • [𝘀𝗼𝗵𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/Mlze1bot) • ──╮\n\n ✧ **اوامر التشغيل بالمجموعة**\n\n• **سهى شغلي + اسم الاغنية او بالرد** \n-› لتشغيل الاغاني فالمجموعة\n\n• **سهى طفيها** او ** ايقاف**\n-› لايقاف تشغيل جميع الصوتيات بالمكالمة\n\n• **سهى الي بعده** او **تخطي**\n-› لتشغيل التالي بالانتظار\n\n • **سهى اص** او **اسكتي**\n-› لكتم صوت الحساب المساعد بالمكالمة\n\n• **سهى تكلمي**\n-› لالغاء الكتم واكمال التشغيل\n\n• **سهى ايقاف مؤقت** او **ايقاف مؤقت**\n -› لايقاف التشغيل بشكل مؤقت\n\n• **سهى كملي** او **استئناف**\n -› لاكمال التشغيل بعد الايقاف المؤقت\n\n╰── • [𝘀𝗼𝗵𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/Mlze1bot) • ──╯""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "", callback_data="fft"),
                    InlineKeyboardButton(
                        "", url=f"https://t.me/Mlze1bot")
                ],[
                    InlineKeyboardButton(
                        "رجوع", callback_data="am"),
                    InlineKeyboardButton(
                        "", callback_data="close"),
                ],[

                    InlineKeyboardButton(
                        "𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂", callback_data="fft"),
                    InlineKeyboardButton(
                        "", callback_data="am"),

               ],
          ]
        ),
    )

@app.on_callback_query(filters.regex("sop"))
async def sop(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك !!", show_alert=True)

    await query.edit_message_text(
       f"""✧ 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑻𝒐 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂\n✧ 𝑱𝒐𝒊𝒏 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 𝒔𝒐𝒉𝒂 𝑻𝒐 𝑺𝒆𝒆 𝑨𝒍𝒍 𝑼𝒑𝒅𝒂𝒕𝒆\n\n- 𝑴𝒂𝒔𝒕𝒆𝒓 -› @Mlze1bot\n- 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 -› @Mlze1bot""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "", callback_data="fft"),
                    InlineKeyboardButton(
                        "", url=f"https://t.me/Mlze1bot")
                ],[
                    InlineKeyboardButton(
                        "◌𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂◌", callback_data="am"),
                    InlineKeyboardButton(
                        "◌ᴅᴇᴠᴇʟᴏᴘᴇʀ◌", url=f"t.me/A_S_A_S_K")
                ],[

                    InlineKeyboardButton(
                        "رجوع", callback_data="settings_helper"),
                    InlineKeyboardButton(
                        "", callback_data="am"),

               ],
          ]
        ),
    )
