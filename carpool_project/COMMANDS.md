# CarPool Project - Commands Reference

## 🚀 Quick Start Commands

### 1. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install django
```

Or if you have a requirements.txt:
```bash
pip install -r requirements.txt
```

### 3. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Collect Static Files (IMPORTANT - Run this after adding CSS/JS)

```bash
python manage.py collectstatic --noinput
```

Or if you want to see prompts:
```bash
python manage.py collectstatic
```

### 5. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Then open: http://127.0.0.1:8000/

### 7. Run Server on Specific Port

```bash
python manage.py runserver 8080
```

## 📋 Complete Setup Sequence

Run these commands in order for first-time setup:

```bash
# 1. Activate virtual environment
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # Linux/Mac

# 2. Install Django (if not already installed)
pip install django

# 3. Create/Apply migrations
python manage.py makemigrations
python manage.py migrate

# 4. Collect static files (CSS, JS, images)
python manage.py collectstatic

# 5. Create admin user (optional)
python manage.py createsuperuser

# 6. Run server
python manage.py runserver
```

## 🔄 After Making Changes

### After Adding/Modifying CSS or JavaScript:

```bash
python manage.py collectstatic
```

### After Modifying Models:

```bash
python manage.py makemigrations
python manage.py migrate
```

### After Adding New Templates or Static Files:

Just refresh your browser (no command needed in development mode)

## 🛠️ Useful Development Commands

### Open Django Shell

```bash
python manage.py shell
```

### Check for Errors

```bash
python manage.py check
```

### Show All URLs

```bash
python manage.py show_urls
```

### Clear Cache (if using cache)

```bash
python manage.py clear_cache
```

### Create New App

```bash
python manage.py startapp app_name
```

## 🗄️ Database Commands

### Reset Database (WARNING: Deletes all data)

```bash
# Delete database file
del db.sqlite3  # Windows
rm db.sqlite3   # Linux/Mac

# Recreate migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser again
python manage.py createsuperuser
```

### View Database in Admin

1. Run server: `python manage.py runserver`
2. Go to: http://127.0.0.1:8000/admin/
3. Login with superuser credentials

## 📦 Production Commands

### Collect Static Files for Production

```bash
python manage.py collectstatic --noinput
```

### Run with Production Settings

```bash
python manage.py runserver --settings=carpool_project.settings_production
```

## 🔍 Troubleshooting Commands

### Check Django Version

```bash
python manage.py version
```

### Check Installed Apps

```bash
python manage.py shell
>>> from django.conf import settings
>>> settings.INSTALLED_APPS
```

### Find Static Files

```bash
python manage.py findstatic css/modern-styles.css
```

## 🌐 Google Maps API Setup Commands

### Set Environment Variable (Windows PowerShell)

```powershell
$env:GOOGLE_MAPS_API_KEY="your-api-key-here"
```

### Set Environment Variable (Windows CMD)

```cmd
set GOOGLE_MAPS_API_KEY=your-api-key-here
```

### Set Environment Variable (Linux/Mac)

```bash
export GOOGLE_MAPS_API_KEY="your-api-key-here"
```

## 📝 Common Workflow

### Daily Development Workflow:

```bash
# 1. Activate virtual environment
venv\Scripts\activate

# 2. Start server
python manage.py runserver

# 3. Make changes to code...

# 4. If you changed models:
python manage.py makemigrations
python manage.py migrate

# 5. If you changed static files:
python manage.py collectstatic
```

## ⚡ Quick Commands Cheat Sheet

| Task | Command |
|------|---------|
| Start server | `python manage.py runserver` |
| Create migrations | `python manage.py makemigrations` |
| Apply migrations | `python manage.py migrate` |
| Collect static | `python manage.py collectstatic` |
| Create admin | `python manage.py createsuperuser` |
| Django shell | `python manage.py shell` |
| Check errors | `python manage.py check` |

## 🎯 Important Notes

1. **Always run `collectstatic` after adding/modifying CSS or JS files**
2. **Run migrations after changing models**
3. **Activate virtual environment before running any commands**
4. **In development, Django serves static files automatically, but `collectstatic` is still recommended**

## 🐛 If Commands Don't Work

1. Make sure virtual environment is activated
2. Make sure you're in the project root directory (where `manage.py` is)
3. Check if Django is installed: `pip list | findstr Django`
4. Try: `python -m django --version`

