:-----------------
:-- get chromium tag
:-----------------
: Arguments
: %1 - tag name
:GetChromiumTag
SETLOCAL
echo GetChromiumTag start
if not exist .\src (
  echo Error getting chromium tag
  GOTO:eof
)
cd .\src

cmd /c git fetch origin
cmd /c git checkout tags/%1
gclient sync --with_branch_heads --nohooks
echo GetChromiumTag done
ENDLOCAL
goto:eof
