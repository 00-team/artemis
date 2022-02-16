from django.contrib.auth.models import User


def username(user: User) -> str:
    try:
        if not user.first_name:
            return user.username

        name = user.first_name

        if user.last_name:
            name += ' ' + user.last_name

        return name
    except:
        return 'Username Not Found'