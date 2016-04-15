:-----------------
:-- build chromium
:-----------------
:BuildChromium
SETLOCAL
set GYP_DEFINES=component=shared_library 
set GYP_GENERATORS=msvs-ninja,ninja
set DEPOT_TOOLS_WIN_TOOLCHAIN=0
set GYP_MSVS_VERSION=2013

call gclient runhooks

ninja -C src\out\Debug chrome
ENDLOCAL
goto:eof