# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Attach-Bot/blob/main/LICENSE

import os
import pyrogram
from pyrogram import Client, filters

FayasNoushad = Client(
    "Telegram Attach Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

FayasNoushad.run()
