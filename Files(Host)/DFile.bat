@echo off

cd "C:\Users\Umesh Kumar\Documents\Python\Downloads"

del /f Data.txt

set /p input= Enter the file Name You Want to Download: 

echo %input%>"C:\Users\Umesh Kumar\Documents\Python\Downloads\DName.txt"
