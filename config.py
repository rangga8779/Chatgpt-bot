import os
API_ID :int = int(os.environ.get("API_ID", None))
API_HASH :str = os.environ.get("API_HASH", "00c8e35df83fefbe7f9e38b8c4f3b0e9")
BOT_TOKEN :str= os.environ.get("BOT_TOKEN", "8307340818:AAGkBAqEbjwtt6nD-WoZ-Qfz1sGrUJU25zg")
UPDATE_CHNL :str = os.environ.get("UPDATE_CHNL", "Gilbertallpthare")
SUPPORT_GRP :str = os.environ.get("SUPPORT_GRP", "the_support_chat")
START_IMG :str = os.environ.get(
    "START_IMG", "https://graph.org/file/d4412c7b411ca8da9e177.jpg"
)

MONGO_DB_URI :str = os.environ.get(
    "MONGO_DB_URI",
    "",
)
OWNER_ID :int= os.environ.get("OWNER_ID", 7056257981)

