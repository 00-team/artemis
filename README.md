# Artemis Project

artemis is amazing :)

## How to setup

make a `secrets.json` file in base directory.
then put your variables on it.

```json
// BASE_DIR/secrets.json

{
    "SECRET_KEY": "RANDOM STRING FOR DJANGO SECRET KEY",
    "BOT_TOKEN": "YOUR TELEGRAM BOT TOKEN",
    "BOT_SECRET": "RANDOM STRING FOR BOT_SECRET",
    "CLIENT_ID": "YOUR TWITTER APP CLIENT ID",
    "CLIENT_SECRET": "YOUR TWITTER APP CLIENT SECRET",
    "TWITTER_BEARER": "YOUR TWITTER BEARER TOKEN"
}

```

\
after that you can run the Django

```bash
python pip install -r requirements.txt 
python manage.py runserver 7000 --insecure
```

if you want to run the bot you need to make directory call `data` in Bot dir \
for short: `mkdir Bot/data`

\
after that you'll need to make `main.json` file inside that data dir

```json
// Bot/data/main.json

{
    "chats": [], 
    "admins": []
}
```

and then you can run the bot

```bash
cd Bot
py run.py
```
