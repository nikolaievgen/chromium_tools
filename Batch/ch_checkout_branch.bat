@echo off
rem input variables
set root_name=chrome
set tag=50.0.2661.75
set depot=depot_tools
set browser=Chromium

rem Create root directory
if exist %root_name% (
  echo Error directory root %root_name% is exist
  GOTO:eof
)
md .\%root_name%
cd .\%root_name%

rem get depot tools
call ..\GetDepotTools.bat

rem set depot tools path
set depot_path=%cd%\%depot%
set path=%path%;%depot_path%

rem fetch chromium
call ..\GetChromiumSource.bat %browser%

if not exist .\%browser%\src (
  echo Error getting chromium source
  GOTO:eof
)

rem get chromium tag
cd .\%browser%
call ..\..\GetChromiumTag.bat %tag%

rem Build browser
rem call ..\..\BuildChromium.bat

pause
goto:eof
