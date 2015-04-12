@echo off

set PYTHONPATH=%PYTHONPATH%;..
set PYTHON=c:\python34\python.exe

%PYTHON% -m unittest discover
