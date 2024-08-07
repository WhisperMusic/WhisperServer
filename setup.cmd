@echo off
goto start

:SETUP_VIRTUAL_ENVIRONMENT
    echo You are running setup without Python Virtual Environment activated & echo.
    choice /c YN /m "Do you want to automatically create new environment (Y/N)? " /n

    if not errorlevel == 1 goto :eof
    
    call:CREATE_VIRTUAL_ENVIRONMENT

    echo To activate Virtual Environment again in another cmd session run the following:
    echo %VIRTUAL_ENV_PATH%\Scripts\activate.bat
    echo.
    
    goto :eof

:CREATE_VIRTUAL_ENVIRONMENT
    set VIRTUAL_ENV_PATH=.venv
    set /p VIRTUAL_ENV_PATH="Path to Virtual Environment [default=.venv]: "

    echo. & echo Creating Virtual Environment . . . & echo.

    python -m venv %VIRTUAL_ENV_PATH%

    if not %errorlevel% == 0 (
        echo. & echo "[ERROR] Failed to create Python Virtual Environment" & echo.
        exit /b %errorlevel%
    ) else echo Successfully created Python Virtual Environment

    call %VIRTUAL_ENV_PATH%\Scripts\activate.bat

    if not %errorlevel% == 0 (
        echo. & echo "[ERROR] Failed to activate Python Virtual Environment in current cmd session" & echo.
        exit /b %errorlevel%
    ) else echo Activated Python Virtual Environment

    %VIRTUAL_ENV_PATH%\Scripts\python.exe -m pip install -r requirements.txt >nul

    if not %errorlevel% == 0 (
        echo. & echo "[ERROR] Failed to install all required dependencies" & echo.
        exit /b %errorlevel%
    ) else echo Successfully installed all required dependencies

    echo.
    goto :eof

:SET_SECRET_KEY
    set /p SECRET_KEY="Now create a secret key for server (will be stored in server/.env): "
    set SERVER_DEBUG=False

    set SECRET_KEY > server/.env
    set SERVER_DEBUG >> server/.env

    goto :eof

:start
if not defined VIRTUAL_ENV call:SETUP_VIRTUAL_ENVIRONMENT

call :SET_SECRET_KEY

echo Successfully set up the server
