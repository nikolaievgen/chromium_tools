:-----------------
:-- fetch chromium source
:-----------------
: Arguments
: %1 - dir name where fetch
:GetChromiumSource
@echo off
SETLOCAL
echo GetChromiumSource start
if exist .\%1 (
  echo Error getting chromium source. Src directory exists
  GOTO:eof
)
md .\%1
cd .\%1
cd
call fetch --nohooks chromium
cd ..
echo GetChromiumSource done
ENDLOCAL
goto:eof
