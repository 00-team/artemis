@echo off

:: set night curly mode in environment variables as dev
:: there is only DEV and BUILD values are exists
set NIGHTCURLY_MODE=DEV
:: set NIGHTCURLY_MODE=BUILD

:: runing the django project
python manage.py runserver 7000