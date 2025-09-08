@echo off
REM Check if virtual environment folder "run" exists
if not exist run (
    echo Creating virtual environment...
    python -m venv run
)

echo Activating virtual environment...
call run\Scripts\activate.bat

echo Installing dependencies...
pip install --upgrade pip
pip install mitmproxy netifaces

echo Running mitmdump...
mitmdump -s run.py
