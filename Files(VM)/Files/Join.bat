@echo off 

cd "C:\Users\Server\Desktop\Server"

del /f Data.txt

set /p DFile=<DName.txt

Path=C:\Users\Server\Desktop\Server\Data\%DFile%

cd "C:\Users\Server\Desktop\Server\"

split_join.py join --source-dir %Path%\Fragments --output a


