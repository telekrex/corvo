REM Quick run script for Windows, just for testing really.
@echo off
set original_dir=%CD%
call venv-win\Scripts\activate.bat
cd source
python GUI.py
pauseCopied!