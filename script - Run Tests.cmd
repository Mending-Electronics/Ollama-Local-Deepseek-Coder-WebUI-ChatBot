@echo off
REM Set the PYTHONPATH to the root of the project
set PYTHONPATH=%cd%

REM Activate the virtual environment
call venv\Scripts\activate

REM Run pytest with pytest-html to generate a report
pytest test --html=tests_report.html --self-contained-html

REM Deactivate the virtual environment
deactivate
