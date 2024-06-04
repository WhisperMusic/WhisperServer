@echo off
goto start

:SETUP_VIRTUAL_ENVIRONMENT
    echo You are running setup without Python Virtual Environment activated
    choice /c YN /m "Do you want to automatically create new environment"

    if errorlevel == 1 call :CREATE_VIRTUAL_ENVIRONMENT
    goto :eof

:CREATE_VIRTUAL_ENVIRONMENT
    set VIRTUAL_ENV_PATH=.venv
    set /p VIRTUAL_ENV_PATH="Path to Virtual Environment [default=.venv]: "

    echo.
    echo Creating Virtual Environment . . . 
    echo.

    python -m venv %VIRTUAL_ENV_PATH% && %VIRTUAL_ENV_PATH%\Scripts\activate && pip install -r requirements.txt

    echo.
    goto :eof

:start
if not defined VIRTUAL_ENV call :SETUP_VIRTUAL_ENVIRONMENT
