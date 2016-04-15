:-----------------
:-- get depot tools
:-----------------
:GetDepotTools
@echo off
SETLOCAL
echo GetDepotTools start
set url_depot=https://src.chromium.org/svn/trunk/tools/depot_tools.zip
set depot=depot_tools
curl %url_depot% --output .\%depot%.zip

if exist %depot% (
  echo Error depot directory %depot% is exist
  GOTO:eof
)
7z x .\%depot%.zip
if not exist .\%depot% (
  echo Error getting depot tools
  GOTO:eof
)
del /q .\%depot%.zip
echo GetDepotTools done
ENDLOCAL
goto:eof
