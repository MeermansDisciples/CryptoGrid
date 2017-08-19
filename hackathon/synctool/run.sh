#!/bin/bash
export PATH=${PATH}:$HOME/hackathon/synctool
./chromedriver &
python autosync.py --port=6666
