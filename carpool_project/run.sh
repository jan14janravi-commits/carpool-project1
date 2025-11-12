#!/bin/bash

echo "Starting CarPool Development Server..."
echo ""

# Activate virtual environment
source venv/bin/activate

# Collect static files (quick check)
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run server
echo ""
echo "Server starting at http://127.0.0.1:8000/"
echo "Press Ctrl+C to stop the server"
echo ""
python manage.py runserver

