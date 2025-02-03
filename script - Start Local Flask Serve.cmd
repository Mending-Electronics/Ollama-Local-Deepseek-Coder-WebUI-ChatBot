@echo off

@title :Local Server Launcher

@echo.
@echo Local server starting on port : 5000 ...
@echo.

REM Open MS Edge on 127.0.0.1:5000 in private
start msedge.exe "http://127.0.0.1:5000/" -inprivate

REM Activate the venv and launch the app.py flask serve on 127.0.0.1:5000
call .venv\Scripts\activate && python app.py
