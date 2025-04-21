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
call venv\Scripts\activate
python3 main.py
