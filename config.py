from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","28164938"))
API_HASH = getenv("API_HASH","d53fd90b87686f713f6adc9428bbb6bb")

BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(getenv("OWNER_ID","5536473064"))

MONGO_DB_URI = getenv("mongodb+srv://iamnobita1:nobitamusic1@cluster0.k08op.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN","NOBITA_MUSIC_SUPPORT")
