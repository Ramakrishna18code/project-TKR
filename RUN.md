# 🚀 Quick Start Guide - Running the Project

## 📋 Prerequisites
- Python 3.8 or higher installed
- Git Bash or any terminal (Windows/Linux/Mac)

---

## 🛠️ Setup Instructions

### Step 1: Create Virtual Environment
```bash
python -m venv venv
```

### Step 2: Activate Virtual Environment

**For Windows (Git Bash):**
```bash
source venv/Scripts/activate
```

**For Windows (Command Prompt):**
```cmd
venv\Scripts\activate
```

**For Linux/Mac:**
```bash
source venv/bin/activate
```

### Step 3: Upgrade pip (Optional but Recommended)
```bash
pip install --upgrade pip
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- Django 5.1.4
- scikit-learn 1.5.2
- pandas 2.2.3
- numpy 2.1.3
- opencv-python-headless 4.10.0.84
- gunicorn 21.2.0
- whitenoise 6.6.0

### Step 5: Create Database Tables
```bash
python manage.py makemigrations
python manage.py migrate
```

This creates the SQLite database and all necessary tables.

### Step 6: Create Demo Users
```bash
python manage.py create_demo_users
```

This creates two test users:
- Username: `demo` / Password: `demo123`
- Username: `testuser` / Password: `test123`

### Step 7: Start the Development Server
```bash
python manage.py runserver
```

---

## ✅ Access the Application

Once the server is running, open your browser and go to:

### 🌐 Main URLs:
- **Homepage:** http://127.0.0.1:8000/
- **User Registration:** http://127.0.0.1:8000/Register1/
- **User Login:** http://127.0.0.1:8000/login/
- **Admin Login:** http://127.0.0.1:8000/service/login/

### 🔑 Login Credentials:

**Regular Users:**
- Username: `demo` | Password: `demo123`
- Username: `testuser` | Password: `test123`

**Admin/Service Provider:**
- Username: `Admin` | Password: `Admin`

---

## 🎯 Complete Command Sequence

If you want to run all commands at once (make sure you're in the project directory):

```bash
# Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate  # For Windows Git Bash

# Install dependencies
pip install -r requirements.txt

# Setup database
python manage.py migrate

# Create demo users
python manage.py create_demo_users

# Run the server
python manage.py runserver
```

---

## 🛑 Stopping the Server

To stop the Django development server:
- Press `CTRL + C` in the terminal

---

## 🔄 Running Again (After Initial Setup)

Once you've completed the setup, you only need to:

```bash
# Activate virtual environment
source venv/Scripts/activate  # Windows Git Bash
# OR
venv\Scripts\activate  # Windows CMD

# Start server
python manage.py runserver
```

---

## 📦 Project Structure

```
project-TKR-main/
├── venv/                          # Virtual environment (created during setup)
├── db.sqlite3                     # Database (created after migrations)
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
├── content_detection/             # Main project settings
├── Remote_User/                   # User app (registration, login, predictions)
├── Service_Provider/              # Admin app (analytics, model training)
├── templates/                     # HTML templates
└── static/                        # CSS, JS, images
```

---

## 🐛 Troubleshooting

### Issue: `python: command not found`
**Solution:** Make sure Python is installed and added to PATH. Try `python3` instead of `python`.

### Issue: `venv/Scripts/activate: No such file or directory`
**Solution:** 
- Make sure you're in the correct project directory
- Check if venv folder was created successfully

### Issue: Port 8000 already in use
**Solution:** 
```bash
# Use a different port
python manage.py runserver 8080
```

### Issue: Database migrations fail
**Solution:**
```bash
# Delete db.sqlite3 and try again
rm db.sqlite3
python manage.py migrate
python manage.py create_demo_users
```

---

## 📱 Features

- ✨ **Auto-Fetch YouTube Data:** Paste video URL and data fills automatically
- 🤖 **AI Content Detection:** ML-based analysis of YouTube content
- 📊 **Analytics Dashboard:** View predictions and statistics
- 👥 **User Management:** Registration and profile management
- 📈 **Admin Panel:** Model training and user analytics

---

## 📝 Notes

- Default database is SQLite (no additional database setup needed)
- Admin credentials are hardcoded: Admin/Admin
- Virtual environment must be activated before running commands
- Server runs on http://127.0.0.1:8000/ by default

---

## 🎓 Need Help?

Refer to these files in the project:
- `README.md` - Project overview and features
- `API_SETUP_QUICK_GUIDE.md` - YouTube API configuration
- `DEPLOYMENT_GUIDE.md` - Production deployment instructions
- `TESTING_GUIDE.md` - Testing guidelines

---

**Happy Coding! 🎉**
