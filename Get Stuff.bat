@ECHO OFF
for /f "tokens=* delims=" %%a in ('git pull') do set output=%%a
if %output%!=Already up-to-date. pause