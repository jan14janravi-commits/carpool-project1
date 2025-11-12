@echo off
echo Starting CarPool Development Server...
echo.

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Collect static files (quick check)
echo Collecting static files...
python manage.py collectstatic --noinput

REM Run server
echo.
echo Server starting at http://127.0.0.1:8000/
echo Press Ctrl+C to stop the server
echo.
python manage.py runserver

