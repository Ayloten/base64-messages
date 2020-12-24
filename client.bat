@echo off
:A
python client.py
timeout /t 1 /nobreak > NUL
goto A