#!/bin/bash

echo "===================================="
echo "CarPool Project Setup Script"
echo "===================================="
echo ""

# Activate virtual environment
echo "[1/6] Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "ERROR: Virtual environment not found!"
    echo "Please create it first: python3 -m venv venv"
    exit 1
fi

# Install dependencies
echo "[2/6] Installing dependencies..."
pip install django
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install Django!"
    exit 1
fi

# Create migrations
echo "[3/6] Creating database migrations..."
python manage.py makemigrations
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create migrations!"
    exit 1
fi

# Apply migrations
echo "[4/6] Applying database migrations..."
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to apply migrations!"
    exit 1
fi

# Collect static files
echo "[5/6] Collecting static files..."
python manage.py collectstatic --noinput
if [ $? -ne 0 ]; then
    echo "WARNING: Failed to collect static files!"
    echo "You may need to run this manually later."
fi

# Complete
echo "[6/6] Setup complete!"
echo ""
echo "===================================="
echo "Next steps:"
echo "1. Create admin user: python manage.py createsuperuser"
echo "2. Run server: python manage.py runserver"
echo "3. Open: http://127.0.0.1:8000/"
echo "===================================="
echo ""

