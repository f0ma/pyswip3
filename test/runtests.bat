@echo off

set PYTHONPATH=%PYTHONPATH%;..
set PYTHON=c:\python34\python.exe

python -m unittest discover -v
