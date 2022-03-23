from json import load

with open('../secrets.json', 'r') as f:
    data = load(f)
    BOT_TOKEN = data['BOT_TOKEN']
    BOT_SECRET = data['BOT_SECRET']
    HEADERS = {'Authorization': BOT_SECRET}
