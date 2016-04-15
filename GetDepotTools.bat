:-----------------
:-- get depot tools
:-----------------
:GetDepotTools
@echo off
SETLOCAL
echo GetDepotTools start
set url_depot=https://storage.googleapis.com/chrome-infra/depot_tools.zip
set depot=depot_tools

if exist %depot% (
  echo Error depot directory %depot% is exist
  GOTO:eof
)

md .\%depot%
cd .\%depot%

: get depot tools
curl %url_depot% --output .\%depot%.zip

: extract depot tools
7z x .\%depot%.zip
: clean
del /q .\%depot%.zip

cd ..

if not exist .\%depot% (
  echo Error getting depot tools
  GOTO:eof
)

echo GetDepotTools done
ENDLOCAL
goto:eof
