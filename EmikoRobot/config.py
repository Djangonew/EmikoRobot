# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os

def get_user_list(config, key):
    with open("{}/EmikoRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]

# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 20247370  # integer value, dont use ""
    API_HASH = "813309fab8cd9fce260ce7269e543bdb"
    TOKEN = "6861812262:AAF48WtPnhHNV9qKybMLT370eabgLpPr4dw"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1748872441  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OPENWEATHERMAP_ID = 22322
    OWNER_USERNAME = "dontnicetry"
    BOT_USERNAME = "nerobot"
    SUPPORT_CHAT = "neroosuport"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1002081701186
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1002081701186
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    ERROR_LOG = -1002081701186

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://ruhwehxs:uUx8rkqaoghtwxwjiVRDc8yJxQ1IJxq6@john.db.elephantsql.com/ruhwehxs"  # needed for any database modules
    MONGO_DB_URI = "mongodb+srv://nerobot:1234@cluster0.t3klmek.mongodb.net/?retryWrites=true&w=majority"  # needed for any database modules
    ARQ_API_URL = "https://arq.hamker.in"
    ARQ_API_KEY = "BCYKVF-KYQWFM-JCMORU-RZWOFQ-ARQ"
    BOT_API_URL = "https://api.telegram.org/bot"
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "w4Y2xp58lSdYxNrOtuLxc_YD~MwAZZ8DEE6CAsBLGhQBHwQGNDwL9WnvhZlHjC6J"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    ALLOW_CHATS = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    HEROKU_APP_NAME = "siap"
    HEROKU_API_KEY = "YES"
    REM_BG_API_KEY = "yahoo"
    LASTFM_API_KEY = "yeah"
    CF_API_KEY = "jk"
    BL_CHATS = []  # List of groups that you want blacklisted.
    SESSION_STRING = "1BVtsOL4Bu6volwhUyn_lCYUeCnindU0t4OrDqlv1yxiqXdwiIDvmROWphCrXjdoy8glzgWuZEZ-7Z3pjHqvm_XaFmWrj4TkHNAwOOhmgIDxDzyDFUGRDH727EV42VSPQerJpbyPBhKfUUnyWA-AqUWAHD_bt21czkUjJrsWse23TSHbHLgJQqnk-mALPtQjoSkVydPk3y1Db52Y3NH39aGpAPYOnPXUUcXIRWAiZId382MHX1Uw8uPgr4jhrqR9QEDVAzrZjWqe9c_n2vosAVuTeJIArN9w-DxT1UjTEGWPhx6E08B5yIpWoXpkGXmS2iOrhUGIlQOTTaSs34CZlOOqMCKVEuhY="
    STRING_SESSION = "1BVtsOL4Bu6volwhUyn_lCYUeCnindU0t4OrDqlv1yxiqXdwiIDvmROWphCrXjdoy8glzgWuZEZ-7Z3pjHqvm_XaFmWrj4TkHNAwOOhmgIDxDzyDFUGRDH727EV42VSPQerJpbyPBhKfUUnyWA-AqUWAHD_bt21czkUjJrsWse23TSHbHLgJQqnk-mALPtQjoSkVydPk3y1Db52Y3NH39aGpAPYOnPXUUcXIRWAiZId382MHX1Uw8uPgr4jhrqR9QEDVAzrZjWqe9c_n2vosAVuTeJIArN9w-DxT1UjTEGWPhx6E08B5yIpWoXpkGXmS2iOrhUGIlQOTTaSs34CZlOOqMCKVEuhY="
    MONGO_PORT = 27017
    MONGO_DB = "Emiko"

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True
