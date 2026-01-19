# 🌐 Live Deployment Guide

## Quick Deploy Options (Free Hosting)

### 🚀 Option 1: Render (Recommended - Easiest)

**Steps:**
1. Push your code to GitHub (already done!)
2. Go to [render.com](https://render.com) and sign up
3. Click **New** → **Web Service**
4. Connect your GitHub repository
5. Configure:
   - **Name**: youtube-content-detection
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn content_detection.wsgi:application`
   - **Environment Variables**:
     - `PYTHON_VERSION` = `3.11.9`
     - `SECRET_KEY` = (generate random string)
     - `DEBUG` = `False`
     - `ALLOWED_HOSTS` = `your-app.onrender.com`
6. Click **Create Web Service**

**Your app will be live at**: `https://your-app.onrender.com`

---

### 🐍 Option 2: PythonAnywhere

**Steps:**
1. Sign up at [pythonanywhere.com](https://pythonanywhere.com)
2. Open a **Bash console**:
```bash
git clone https://github.com/YOUR-USERNAME/youtube-content-detection-ai.git
cd youtube-content-detection-ai
mkvirtualenv --python=/usr/bin/python3.10 venv
pip install -r requirements.txt
python manage.py collectstatic --noinput
```

3. Go to **Web** tab → **Add a new web app**
4. Choose **Manual configuration** → Python 3.10
5. Configure:
   - **Source code**: `/home/yourusername/youtube-content-detection-ai`
   - **Working directory**: `/home/yourusername/youtube-content-detection-ai`
   - **Virtualenv**: `/home/yourusername/.virtualenvs/venv`

6. Edit **WSGI configuration file**:
```python
import sys
import os

path = '/home/yourusername/youtube-content-detection-ai'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'content_detection.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

7. Click **Reload** your web app

**Your app will be live at**: `https://yourusername.pythonanywhere.com`

---

### ☁️ Option 3: Railway

**Steps:**
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click **New Project** → **Deploy from GitHub repo**
4. Select your repository
5. Railway auto-detects Django and deploys!
6. Add environment variables:
   - `SECRET_KEY` = (random string)
   - `DEBUG` = `False`

**Your app will be live at**: Generated Railway URL

---

### 🔵 Option 4: Vercel (with Database)

**Steps:**
1. Install Vercel CLI:
```powershell
npm install -g vercel
```

2. Create `vercel.json`:
```json
{
  "builds": [
    {
      "src": "content_detection/wsgi.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "content_detection/wsgi.py"
    }
  ]
}
```

3. Deploy:
```powershell
vercel --prod
```

---

## 📋 Pre-Deployment Checklist

✅ **Environment variables set**
✅ **Static files configured** (WhiteNoise added)
✅ **Production dependencies** (gunicorn added)
✅ **DEBUG = False** in production
✅ **SECRET_KEY** is environment variable
✅ **Database migrations run**
✅ **Allowed hosts configured**

---

## 🔧 Before Going Live

### 1. Collect Static Files
```powershell
python manage.py collectstatic --noinput
```

### 2. Run Migrations
```powershell
python manage.py migrate
```

### 3. Create Superuser
```powershell
python manage.py createsuperuser
```

---

## 🌍 Environment Variables

For production, set these environment variables:

| Variable | Value | Description |
|----------|-------|-------------|
| `SECRET_KEY` | Random 50-char string | Django secret key |
| `DEBUG` | `False` | Disable debug mode |
| `ALLOWED_HOSTS` | `your-domain.com` | Your domain name |
| `DATABASE_URL` | PostgreSQL URL | If using PostgreSQL |

**Generate SECRET_KEY:**
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

---

## 🗄️ Using PostgreSQL (Production Database)

### Update requirements.txt:
```
psycopg2-binary==2.9.9
dj-database-url==2.1.0
```

### Update settings.py:
```python
import dj_database_url

if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

---

## 🔒 Security Best Practices

1. **Never commit sensitive data**
2. **Use environment variables** for secrets
3. **Enable HTTPS** (most platforms do this automatically)
4. **Set secure cookies**:
```python
# Add to settings.py for production
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

---

## 🐛 Troubleshooting

### Static Files Not Loading?
```powershell
python manage.py collectstatic --noinput
```

### Database Errors?
```powershell
python manage.py migrate
```

### 500 Server Error?
- Check platform logs
- Ensure DEBUG=False
- Verify environment variables

---

## 📊 Monitoring

- **Render**: Built-in logs and metrics
- **PythonAnywhere**: Access logs via dashboard
- **Railway**: Real-time logs in dashboard

---

## 🎉 You're Ready!

Choose your platform and deploy in minutes. All configuration files are already created:
- ✅ `render.yaml` - For Render
- ✅ `Procfile` - For Heroku/Railway
- ✅ `runtime.txt` - Python version
- ✅ `requirements.txt` - Updated with production deps
- ✅ `settings.py` - Production-ready

**Happy Deploying! 🚀**
