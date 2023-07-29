@echo off

cd "C:\Users\Server\Desktop\Server"

set /p File=<Name.txt

rename a.E01 %File%

cd "C:\Users\Server\Desktop\Server"

Path= C:\Users\Server\Desktop\Server\Data\%File%

split_join.py split --file %File% --destination %Path%\Fragments --size 1400000

del /f %File%

move Name.txt %Path%