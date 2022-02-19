# from hashlib import sha256
# from typing import Literal

from json import load
from json import dump
from os.path import exists
from logging import getLogger

# from sqlite3 import Cursor, connect
# from hashids import Hashids
# from string import hexdigits

USER_DB = './data/users.db'

logger = getLogger(__name__)


def read_json(filename: str, default=None):
    if exists(filename):
        with open(filename, 'r') as f:
            return load(f)

    return default


def write_json(filename: str, json):
    with open(filename, 'w') as f:
        dump(json, f)


# LANG = Literal['en', 'ru', None]

# def make_users_table(cur: Cursor):
#     table = '''CREATE TABLE users (
#         id INTEGER unique,
#         lang VARCHAR(2),
#         invite VARCHAR(64) unique,
#         total_invites INTEGER)'''

#     try:
#         cur.execute(
#             'SELECT name FROM sqlite_master WHERE type="table" AND name="users"'
#         )
#         if not cur.fetchone():
#             cur.execute(table)
#     except:
#         pass

# def get_invite(user_id):
#     return hashid.encode(user_id)

# def get_user(cur, user_id):
#     cur.execute(
#         'SELECT * FROM users WHERE id=:user_id',
#         {'user_id': user_id},
#     )

#     return cur.fetchone()

# def check_user(cur, user_id):
#     user = get_user(cur, user_id)

#     if user:
#         return user

#     cur.execute(
#         'INSERT INTO users VALUES (?, "en", inv(?), 0)',
#         (user_id, user_id),
#     )

#     return get_user(cur, user_id)

# def update_user(user_id, lang: LANG = None, total_invites=0):
#     con = connect(USER_DB)
#     con.create_function('inv', 1, get_invite)
#     cur = con.cursor()

#     make_users_table(cur)

#     user_exists = bool(get_user(cur, user_id))
#     user = check_user(cur, user_id)

#     if lang and user[1] != lang:
#         cur.execute(
#             'UPDATE users SET lang = ? WHERE id = ?',
#             (lang, user_id),
#         )
#         user = get_user(cur, user_id)

#     if total_invites and user[3] != total_invites:
#         cur.execute(
#             'UPDATE users SET total_invites = ? WHERE id = ?',
#             (total_invites, user_id),
#         )
#         user = get_user(cur, user_id)

#     con.commit()
#     con.close()

#     return (user_exists, user)


def update_data(chats):
    try:
        filename = './data/main.json'
        data = read_json(filename)

        if not data:
            raise ValueError('data file not found')

        data['chats'] = chats

        write_json(filename, data)
    except Exception as e:
        logger.error(e)


def get_token() -> str:
    # global hashid
    with open('../secrets.json', 'r') as f:
        return load(f)['BOT_TOKEN']

    # hashid = Hashids(salt=token, min_length=12, alphabet=hexdigits)

    # return token