#!/bin/bash
echo "Welcome to Python 3D."
echo "-- Instructions / Information --"
echo "use the W A S D keys to move to camera"
echo "use the SPACE and LSHIFT keys to go up and down"
echo "use the mouse or the arrow keys to look around"
echo "use the F key to toggle fullscreen."
echo "use ESC to exit the game. [Important]"
echo "--------------------------------"
read -pr "Press [Enter] to continue . . ."
echo "Setting up environment."
python3 -m venv venv
./venv/bin/activate
echo "Getting required libraries."
pip install -r requirments.txt
echo "Starting Program."
python3 main.py