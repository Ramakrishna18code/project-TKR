# YouTube API Setup - Step by Step Guide

## Quick Setup (5 minutes)

### Step 1: Get Your YouTube API Key

1. **Go to Google Cloud Console**
   - Open: https://console.cloud.google.com/

2. **Create a Project** (if you don't have one)
   - Click "Select a project" at the top
   - Click "NEW PROJECT"
   - Name: "YouTube Content Detection"
   - Click "CREATE"

3. **Enable YouTube Data API v3**
   - In the search bar, type: "YouTube Data API v3"
   - Click on "YouTube Data API v3"
   - Click "ENABLE" button

4. **Create API Credentials**
   - Click "CREATE CREDENTIALS" button
   - Select "API Key"
   - Copy the generated API key
   - Click "CLOSE"

### Step 2: Add API Key to Your Project

Open the file: `config.py` in your project folder and replace:

```python
YOUTUBE_API_KEY = 'YOUR_YOUTUBE_API_KEY_HERE'
```

With your actual API key:

```python
YOUTUBE_API_KEY = 'AIzaSyDxxxxxxxxxxxxxxxxxxxxxxxxxx'  # Your actual key
```

### Step 3: Restart the Server

Press `CTRL+C` in the terminal to stop the server, then run:
```
python manage.py runserver
```

### Step 4: Test It!

1. Go to: http://127.0.0.1:8000/Predict_YouTube_Content_Type/
2. Paste ONLY the YouTube link: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
3. Click "Analyze Content with AI"
4. **All data will be fetched automatically!** ✨

---

## Important Notes:

- **Free Tier**: 10,000 API calls per day (more than enough for testing)
- **No Credit Card Required** for basic usage
- **Takes only 5 minutes** to set up
- Once configured, you'll NEVER need to enter data manually again!

## Need Help?

If you see any errors, check the terminal output for detailed messages.
