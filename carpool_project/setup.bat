@echo off
echo ====================================
echo CarPool Project Setup Script
echo ====================================
echo.

REM Activate virtual environment
echo [1/6] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Virtual environment not found!
    echo Please create it first: python -m venv venv
    pause
    exit /b 1
)

REM Install dependencies
echo [2/6] Installing dependencies...
pip install django
if errorlevel 1 (
    echo ERROR: Failed to install Django!
    pause
    exit /b 1
)

REM Create migrations
echo [3/6] Creating database migrations...
python manage.py makemigrations
if errorlevel 1 (
    echo ERROR: Failed to create migrations!
    pause
    exit /b 1
)

REM Apply migrations
echo [4/6] Applying database migrations...
python manage.py migrate
if errorlevel 1 (
    echo ERROR: Failed to apply migrations!
    pause
    exit /b 1
)

REM Collect static files
echo [5/6] Collecting static files...
python manage.py collectstatic --noinput
if errorlevel 1 (
    echo WARNING: Failed to collect static files!
    echo You may need to run this manually later.
)

REM Create superuser (optional)
echo [6/6] Setup complete!
echo.
echo ====================================
echo Next steps:
echo 1. Create admin user: python manage.py createsuperuser
echo 2. Run server: python manage.py runserver
echo 3. Open: http://127.0.0.1:8000/
echo ====================================
echo.
pause

