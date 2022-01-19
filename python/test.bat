@echo off

bitsadmin /transfer "test" https://registry.npmjs.org/buffer-queue/-/buffer-queue-1.0.0.tgz "%~dp0\buffer-queue-1.0.0.tgz" > nul
call:CheckError

call:Log "ok"

pause
exit

:CheckError
IF not "%errorlevel%"=="0" (
	call:Log "error!!"
	pause
	exit
)

:Log
echo %1