@echo off

if not defined VIRTUAL_ENV (
    if exist .venv (
        call .venv/Scripts/activate.bat
    )
)

python ./server/manage.py runserver
