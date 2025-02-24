from os import environ, getenv
import re
import os

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "6717382350"))
SILICON_PIC = os.environ.get("SILICON_PIC", "https://envs.sh/twJ.jpg")
API_ID = int(getenv("API_ID", "26162072"))
API_HASH = str(getenv("API_HASH", "ba25181c01b50d945748801b6c8b6ecc"))
BOT_TOKEN = str(getenv("BOT_TOKEN", ""))
FORCE_SUB = os.environ.get("FORCE_SUB", "RM_Botz") 
MONGO_DB = str(getenv("MONGO_DB", "mongodb+srv://rebelbotz22:vNcEEoNvSQ33d44K@cluster0.oj1hu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",))
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b>File Name:- `{file_name}`\n\n{file_size}</b>",
    )
)
