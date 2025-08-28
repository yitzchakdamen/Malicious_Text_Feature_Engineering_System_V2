
@echo off

set "FOLDER=C:\Users\isaac\source\repos\Malicious_Text_Feature_Engineering_System_V2\scripts"

for %%f in ("%FOLDER%\*.bat") do (
    echo run: %%~nxf
    call "%%f"
)

pause


