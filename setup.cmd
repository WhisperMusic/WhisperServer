@echo off
goto start

:SETUP_VIRTUAL_ENVIRONMENT
    echo You are running setup without Python Virtual Environment activated & echo.
    choice /c YN /m "Do you want to automatically create new environment (Y/N)? " /n

    if errorlevel == 1 call:CREATE_VIRTUAL_ENVIRONMENT
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

    %VIRTUAL_ENV_PATH%\Scripts\python.exe -m pip install -r requirements.txt

    if not %errorlevel% == 0 (
        echo. & echo "[ERROR] Failed to install all required dependencies" & echo.
        exit /b %errorlevel%
    ) else echo Successfully installed all required dependencies

    echo.
    goto :eof

:start
if not defined VIRTUAL_ENV call:SETUP_VIRTUAL_ENVIRONMENT
