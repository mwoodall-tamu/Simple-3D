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

:: Use "where" to find Python installations in PATH
for /f "delims=" %%i in ('where python') do (
    set PYTHON_PATH=%%i
    call :check_python
)

:: If no suitable Python installation is found, show an error
echo No supported Python 3 installation found.
goto :eof

:check_python
:: Check if the path belongs to the Microsoft Store Python (Microsoft Store Python installs under %USERPROFILE%\AppData\Local\Microsoft\WindowsApps)
echo %PYTHON_PATH% | findstr /i "%USERPROFILE%\AppData\Local\Microsoft\WindowsApps" >nul
if %errorlevel%==0 (
    echo Using Microsoft Store Python at %PYTHON_PATH%
    goto :use_python
)

:: Check if the path is a standard CPython install (typically in %ProgramFiles% or %AppData%\Local\Programs\Python)
echo %PYTHON_PATH% | findstr /i "C:\Program Files\Python" >nul
if %errorlevel%==0 (
    echo Using standard Python at %PYTHON_PATH%
    goto :use_python
)

:: If neither of the above, skip this installation (likely MSYS, Anaconda, or another non-standard install)
echo Skipping un-supported Python at %PYTHON_PATH%
goto :eof

:use_python
:: Create and activate a virtual environment using the identified Python
"%PYTHON_PATH%" -m venv venv
call venv\Scripts\activate

:: Upgrade pip and install requirements
python -m pip install --upgrade pip
pip install -r requirements.txt

:: Run your Python script
python main.py
goto :eof
