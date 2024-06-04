@echo off
goto start

:SETUP_VIRTUAL_ENVIRONMENT
    echo You are running setup without Python Virtual Environment activated
    choice /c YN /m "Do you want to automatically create new environment"

    if errorlevel == 1 call :CREATE_VIRTUAL_ENVIRONMENT
    goto :eof

:CREATE_VIRTUAL_ENVIRONMENT
    set /p _venv_path="Path to Virtual Environment [default=.venv]: "


    if not defined _venv_path set _venv_path=.venv

    echo.
    echo Creating Virtual Environment . . . 
    echo.

    python -m venv %_venv_path% && %_venv_path%\Scripts\activate && pip install -r requirements.txt

    echo.
    goto :eof

:start
if not defined VIRTUAL_ENV call :SETUP_VIRTUAL_ENVIRONMENT
