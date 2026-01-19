# YouTube Content Detection - Setup Guide

## New Features Added

### 🎯 Content Verification with Likes/Dislikes Display

After uploading a video link, the system now:
1. **Automatically fetches video data** from YouTube API (if configured)
2. **Verifies content authenticity** - Determines if content is "True" or "False"
3. **Displays comprehensive analytics**:
   - Video Title
   - Channel Name
   - Views Count
   - Likes Count
   - Dislikes Count
   - Comments Count
   - Confidence Level

## Setup Instructions

### 1. YouTube API Key Configuration (Optional but Recommended)

To enable automatic video data fetching:

1. **Get a YouTube API Key**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the **YouTube Data API v3**:
     - Navigate to "APIs & Services" > "Library"
     - Search for "YouTube Data API v3"
     - Click "Enable"
   - Create credentials:
     - Go to "APIs & Services" > "Credentials"
     - Click "Create Credentials" > "API Key"
     - Copy the generated API key

2. **Add API Key to config.py**:
   ```python
   # Open config.py and replace the placeholder
   YOUTUBE_API_KEY = 'your_actual_api_key_here'
   ```

### 2. How to Use

#### Method 1: With YouTube API (Automatic)
1. Simply paste a YouTube video URL in the "YouTube Video Link" field
2. Click "Analyze Content with AI"
3. The system will:
   - Automatically extract the video ID
   - Fetch all video details from YouTube
   - Analyze the content
   - Display results with likes/dislikes

#### Method 2: Manual Entry (Fallback)
If YouTube API is not configured:
1. Paste the video link
2. Manually fill in the video details:
   - Title
   - Channel Name
   - Content Description
   - Engagement metrics (views, likes, dislikes, comments)
3. Click "Analyze Content with AI"

### 3. Content Detection Logic

The system analyzes content using keyword-based detection:

**Inappropriate Keywords Checked**:
- violence, explicit, adult, inappropriate, harmful
- abuse, hate, racist, porn, drug, weapon
- kill, murder, blood, gore, nsfw

**Detection Criteria**:
- **False Content** (High Confidence): 2+ inappropriate keywords found
- **False Content** (Medium Confidence): 1 inappropriate keyword found
- **True Content** (High Confidence): No inappropriate keywords found

### 4. Results Display

After analysis, you'll see:

#### ✅ True Content
- Green success message
- Shield icon
- Full engagement metrics
- Video link to watch on YouTube

#### ⚠️ False Content
- Red warning message
- Warning icon
- Full engagement metrics
- Video link for verification

### 5. Packages Installed

```
Django==5.1.4
scikit-learn==1.5.2
pandas==2.2.3
numpy==2.1.3
opencv-python==4.10.0.84
google-api-python-client (NEW)
isodate (NEW)
```

## Usage Examples

### Example YouTube URLs to Test:
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://youtu.be/dQw4w9WgXcQ
https://www.youtube.com/embed/dQw4w9WgXcQ
```

## Troubleshooting

### YouTube API Not Working?
- Check if API key is correctly set in config.py
- Ensure YouTube Data API v3 is enabled in Google Cloud Console
- Check API quota limits (default: 10,000 units/day)
- Manual entry will still work as fallback

### No Likes/Dislikes Showing?
- YouTube removed public dislike counts in 2021
- Likes should still display for most videos
- Manual entry allows you to input historical data

## Security Notes

⚠️ **Important**: Keep your API key secure!
- Never commit config.py to public repositories
- Add config.py to .gitignore
- Consider using environment variables in production

## Future Enhancements

Possible improvements:
- Machine learning model training for better accuracy
- Sentiment analysis integration
- Category-specific detection rules
- User feedback mechanism
- Historical data tracking
- Batch video analysis

---

**Need Help?** Check the Django logs for detailed error messages.
