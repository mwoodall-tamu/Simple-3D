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
echo Setting up python environment
%UserProfile%\AppData\Local\Microsoft\WindowsApps\python3.exe -m venv venv
echo Setup complete!
call venv\Scripts\activate
echo Loading required Libraries. This might take a while . . .
pip install -r requirments.txt
echo Libraries loaded, starting program.
python3 main.py
