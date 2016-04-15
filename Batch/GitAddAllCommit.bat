:-----------------
:-- git add all chromium changes and commit
:-----------------
: Arguments
: %1 - ver name
:GitAddAllCommit
@echo off
SETLOCAL
set ver==50.0.2661.75
set message="Chromium %ver%"

echo GitAddAllCommit start
if not exist .\src (
  echo Error git commit changes
  GOTO:eof
)

cmd /c git add --all
cmd /c git add -u
git commit -m %message%
echo GitAddAllCommit done
ENDLOCAL
goto:eof