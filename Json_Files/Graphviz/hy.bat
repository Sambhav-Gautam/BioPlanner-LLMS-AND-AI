@echo off
setlocal enabledelayedexpansion

rem Set the directory where your .dot files are located
set "dot_dir=C:\Users\sambh\OneDrive\Desktop\Json_Files\Graphviz"

rem Create RESULTS directory if it doesn't exist
if not exist "%dot_dir%\RESULTS" (
    mkdir "%dot_dir%\RESULTS"
)

rem Loop through each .dot file and convert it to .png using simplified command
for %%F in ("%dot_dir%\*.dot") do (
    echo Converting %%~nxF to PNG...
    dot -Tpng "%%F" -o "%dot_dir%\RESULTS\%%~nF.png"
)

echo Conversion complete!
pause
