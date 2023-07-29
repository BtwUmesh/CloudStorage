@echo off

cd "C:\Users\Umesh Kumar\Documents\Python"

dir

set /p input= Enter the file Name: 

mkdir Temp

echo %input%>"C:\Users\Umesh Kumar\Documents\Python\Temp\Name.txt"

copy %input% "C:\Users\Umesh Kumar\Documents\Python\Temp"
 
cd "C:\Users\Umesh Kumar\Documents\Python\Temp"

rename %input% a.E01