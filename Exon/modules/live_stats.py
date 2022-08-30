"""
MIT License

Copyright (c) 2022 ABISHNOI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# ""DEAR PRO PEOPLE,  DON'T REMOVE & CHANGE THIS LINE
# TG :- @Abishnoi1M 
#     MY ALL BOTS :- Abishnoi_bots
#     GITHUB :- KingAbishnoi ""

from pymongo import MongoClient
from pyrogram import *
from pyrogram.types import *

import Exon.modules.sql.users_sql as sql
from Exon import MONGO_DB_URI, pgram

worddb = MongoClient(MONGO_DB_URI)
k = worddb["Exonstats"]["live_stats"]


@pgram.on_message(
    filters.text & ~filters.private,
)
async def live(client: Client, message: Message):
    is_live = k.find_one({"live": "stats"})
    users = f"{sql.num_users()}"
    chats = f"{sql.num_chats()}"
    captionk = (
        f"ʟɪᴠᴇ ᴀsᴜx sᴛᴀᴛs\n\n• {sql.num_users()} ᴜsᴇʀs, ᴀᴄʀᴏss {sql.num_chats()} ᴄʜᴀᴛs"
    )
    if not is_live:
        k.insert_one({"live": "stats", "user": users, "chat": chats})
        await pgram.edit_message_text(
            chat_id=-1001557334564, #channel id
            message_id=67,  #channel msg id
            text=captionk,
            disable_web_page_preview=True,
        )
    if is_live:
        is_live2 = k.find_one({"live": "stats", "user": users, "chat": chats})
        if not is_live2:
            k.update_one({"live": "stats"}, {"$set": {"user": users, "chat": chats}})
            # editing chat_id and message id
            await pgram.edit_message_text(
                chat_id=-1001557334564, #hear your channel id
                message_id=67,  # Channel msg id
                text=captionk,
                disable_web_page_preview=True,
            )









