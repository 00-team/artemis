# Artemis Project

artemis is amazing :)

## How to setup

make a `secret.py` file in artemis directory.
then put your variables on it.

```py
# artemis/secret.py

SECRET_KEY = 'YOUR-SECRET-KEY'
```

\
after that run the Django

```bash
python pip install -r requirements.txt 
python manage.py runserver 7000 --insecure
```
