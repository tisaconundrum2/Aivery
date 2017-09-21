md chatter\ui
echo off && cls
for /r %%i in ("*.ui") do pyuic5 -x "%%i" > chatter\ui\%%~ni.py