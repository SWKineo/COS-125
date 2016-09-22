git add --all
set /p message=Git Commit Message: 
git commit -m "%message%"
:PUSH
git push -u origin master
GOTO PUSH
pause