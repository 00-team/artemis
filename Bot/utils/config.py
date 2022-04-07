from json import load
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


with open(BASE_DIR / 'secrets.json', 'r') as f:
    data = load(f)
    BOT_TOKEN = data['BOT_TOKEN']
    BOT_SECRET = data['BOT_SECRET']
    HEADERS = {'Authorization': BOT_SECRET}

HOST = 'http://127.0.0.1:7000/'
