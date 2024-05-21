from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN", "6571199121:AAGyGOXDBfA17LPYsTzZX9_8AoTPCbl20JI") 
API_ID = int(getenv("API_ID", "26108237"))
API_HASH = getenv("API_HASH", "b69fac6842079a15c7b51b16f70cf77e")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Anishkhamrui76:Anishkhamrui76@cluster0.ezysgve.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1822479202 1412758888").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "1822479202").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001745060879"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Anish_music_bot")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "HRKU-49877318-229b-4837-8135-cad20d93a813")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "music-foyruii")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/jankarikiduniya/TG-Music")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))


if str(getenv("STRING_SESSION1")).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))
