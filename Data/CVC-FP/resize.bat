@echo off
for %%f in (%*) do (
    echo %%~f
    "C:\Program Files\Inkscape\inkscape.exe" ^
    %%~f -e "%%~dpnf.png" --export-area-drawing
)