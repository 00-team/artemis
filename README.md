# Nightcurly Project

Nightcurly ...

## How to setup

make a `secrets.json` file in base directory.
then put your variables on it.

```json
// BASE_DIR/secrets.json

{
    "SECRET_KEY": "django random secret key",

    "BOT": {
        "TOKEN": "your telegram bot token",
        "SECRET": "bot random secret",
        "USERNAME": "your bot username"
    },

    "TWITTER": {
        "CLIENT_ID": "twitter api client id",
        "CLIENT_SECRET": "twitter api client secret",
        "BEARER_TOKEN": "twitter api bearer token"
    },

    "WEBHOOKS": {
        "ACCOUNT": ["a list or a single url for discord account webhooks"],
        "ERROR": "a list or a single url for discord account webhooks"
    },

    "DEV": {
        "INTERNAL_HOST": "127.0.0.1:8000", // sample
        "EXTERNAL_HOST": "localhost:8000" // sample
    },

    "BUILD": {
        "INTERNAL_HOST": "0.0.0.0", // a local ip for connecting the bot to django ...
        "EXTERNAL_HOST": "your server ip OR your domain name",
        "ALLOWED_HOSTS": ["django allowed hosts"]
    }
}
```

\
after that you can run the Django

```bash
# set your env mode | DEV or BUILD
NIGHTCURLY_MODE="DEV"
pip install -r requirements.txt
python manage.py runserver 7000
```

you can run the bot with:

```bash
cd Bot
py run.py
```
