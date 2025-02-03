@echo off

@title :Local Server Launcher

@echo.
@echo Local server starting on port : 5000 ...
@echo.

start msedge.exe "http://127.0.0.1:5000/" -inprivate
call .venv\Scripts\activate && python app.py
