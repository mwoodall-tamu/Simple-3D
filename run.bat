@echo off
echo Welcome to Simple 3D.
echo -- Instructions / Information --
echo use the W A S D keys to move to camera
echo use the SPACE and LSHIFT keys to go up and down
echo use the mouse or the arrow keys to look around
echo use the F key to toggle fullscreen
echo use ESC to exit the game. (Important)
echo --------------------------------
pause

set PYTHON_PATH=%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\python.exe

if exist "%PYTHON_PATH%" (
    echo Python found at %PYTHON_PATH%
    
    %PYTHON_PATH% -m venv venv
    call venv\Scripts\activate

    python -m pip install --upgrade pip
    pip install -r requirements.txt

    python main.py
) else (
    echo Official Microsoft installation of Python not detected.
    pause
)
