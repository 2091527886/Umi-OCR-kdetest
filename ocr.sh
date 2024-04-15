#!/bin/bash
while [[ -z "$(/usr/bin/pgrep plasmashell -n -U $UID)" ]]; do sleep 3; done

# Export the current desktop session environment variables
# Sometimes it try to change $UID so we must remove -e option at the shebang or use 2>/dev/null here
export $(sudo /usr/bin/xargs -0 -a "/proc/$(/usr/bin/pgrep plasmashell -n -U $UID)/environ") 2>/dev/null
cd /home/temp/Umi-OCR-1/UmiOCR-data/py_src/
source ./venv/bin/activate
cd /home/temp/Umi-OCR-1/UmiOCR-data/
screen -dmS hideavd   zsh -c  "sleep 10;qdbus org.kde.KWin /Scripting org.kde.kwin.Scripting.loadScript /home/temp/Umi-OCR-1/close.js;qdbus org.kde.KWin /Scripting org.kde.kwin.Scripting.start;"
python /home/temp/Umi-OCR-1/UmiOCR-data/main1.py 
