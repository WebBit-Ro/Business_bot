import os
import re

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
MANAGER_USERNAME = os.getenv("MANAGER_USERNAME", "").strip().lstrip("@")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing. Add it to your .env file.")

if not re.fullmatch(r"[A-Za-z0-9_]{5,32}", MANAGER_USERNAME):
    raise ValueError(
        "MANAGER_USERNAME must be a valid Telegram username without @."
    )
