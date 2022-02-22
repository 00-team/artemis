from sqlite3 import connect
from typing import Literal

from hashlib import sha1

users_db = './data/users.db'


class User:
    LANG = Literal['en', 'ru']

    table = '''CREATE TABLE users (
        id INTEGER UNIQUE, 
        lang VARCHAR(2), 
        invite VARCHAR(40) UNIQUE, 
        total_invites INTEGER)'''

    user_id: int
    user_exists: bool
    lang: LANG
    invite: str
    total_invites: int

    def __init__(self, user_id):
        self.user_id = user_id
        self.setup_table()
        self.check_user()

    def setup_table(self):
        con = connect(users_db)
        cur = con.cursor()

        try:
            cur.execute(
                'SELECT name FROM sqlite_master WHERE type="table" AND name="users"'
            )
            if not cur.fetchone():
                cur.execute(self.table)
        except:
            pass

        con.commit()
        con.close()

    def hash_invite(self):
        inv = str(self.user_id).encode()
        return sha1(inv).hexdigest()

    def get_user(self):
        con = connect(users_db)
        cur = con.cursor()

        cur.execute(
            'SELECT * FROM users WHERE id=:user_id',
            {'user_id': self.user_id},
        )
        user = cur.fetchone()
        con.close()

        if user:
            self.lang = user[1]
            self.invite = user[2]
            self.total_invites = user[3]

        return user

    def check_user(self):
        user = self.get_user()

        con = connect(users_db)
        cur = con.cursor()

        if user:
            self.user_exists = True
            return

        self.user_exists = False
        inv = self.hash_invite()

        cur.execute(
            'INSERT INTO users VALUES (?, "en", ?, 0)',
            (self.user_id, inv),
        )

        con.commit()
        con.close()

        self.get_user()

    def update(self, lang: LANG = None, total_invites: int = None):
        self.get_user()

        lang = str(lang)

        if len(lang) != 2:
            lang = self.lang

        if not isinstance(total_invites, int):
            total_invites = self.total_invites

        if lang != self.lang or total_invites != self.total_invites:
            con = connect(users_db)
            cur = con.cursor()
            cur.execute(
                'UPDATE users SET lang = ?, total_invites = ? WHERE id = ?',
                (lang, total_invites, self.user_id),
            )
            con.commit()
            con.close()
            self.get_user()


def user_by_invite(invite: str) -> User | None:
    con = connect(users_db)
    cur = con.cursor()
    cur.execute(
        'SELECT * FROM users WHERE invite=:invite',
        {'invite': invite},
    )
    user = cur.fetchone()
    con.close()

    if not user:
        return None

    return User(user[0])


def user_by_id(user_id: int) -> User | None:
    con = connect(users_db)
    cur = con.cursor()
    cur.execute(
        'SELECT * FROM users WHERE id=:user_id',
        {'user_id': user_id},
    )
    user = cur.fetchone()
    con.close()

    if not user:
        return None

    return User(user[0])