# 📊 Testing Guide - How to Fill the Form Correctly

## The Issue
You're seeing **0** for all engagement metrics (Views, Likes, Dislikes, Comments) because the data isn't being entered correctly.

## ✅ Solution - How to Fill the Form

### Step 1: Open a YouTube Video
Go to any YouTube video, for example:
- https://www.youtube.com/watch?v=dQw4w9WgXcQ

### Step 2: Copy These Exact Values:

**From the video page, copy:**

1. **Video Link** (URL bar):
   ```
   https://www.youtube.com/watch?v=dQw4w9WgXcQ
   ```

2. **Title** (above video):
   ```
   Rick Astley - Never Gonna Give You Up (Official Video)
   ```

3. **Channel Name** (below video):
   ```
   Rick Astley
   ```

4. **Description** (click "...more" to expand):
   ```
   The official video for "Never Gonna Give You Up" by Rick Astley...
   ```

5. **Views** (below video, just the number):
   ```
   1234567890
   ```
   ⚠️ **Important:** Enter ONLY the number, no commas, no text

6. **Likes** (thumbs up button):
   ```
   14000000
   ```
   ⚠️ **Important:** Enter ONLY the number

7. **Dislikes** (if visible):
   ```
   500000
   ```
   ⚠️ **Important:** Enter ONLY the number, or leave 0

8. **Comments** (in comments section):
   ```
   2500000
   ```
   ⚠️ **Important:** Enter ONLY the number

## ❌ Common Mistakes

**DON'T DO THIS:**
- ❌ Views: "1.2M views" ← Wrong! (has text)
- ❌ Views: "1,234,567" ← Wrong! (has commas)
- ❌ Likes: "14K" ← Wrong! (abbreviated)

**DO THIS:**
- ✅ Views: 1234567 ← Correct! (only numbers)
- ✅ Likes: 14000 ← Correct! (full number)
- ✅ Comments: 2500 ← Correct! (exact number)

## 🎯 Quick Test Data

If you just want to test quickly, use these values:

```
Video Link: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Title: Test Video
Channel: Test Channel
Description: This is a family-friendly educational video for kids
Views: 1000000
Likes: 50000
Dislikes: 1000
Comments: 25000
```

## 🔧 Debugging Steps

1. **Fill the form with the test data above**
2. **Click "Analyze Content with AI"**
3. **Check the results page:**
   - You should see Views: 1,000,000 (formatted with commas)
   - You should see Likes: 50,000
   - You should see Dislikes: 1,000
   - You should see Comments: 25,000

## 💡 Pro Tip

**If you want automatic filling:**
1. Get YouTube API key from https://console.cloud.google.com/
2. Add it to `config.py`
3. Just paste the YouTube link
4. Wait 1-2 seconds
5. All fields will auto-fill! ✨

---

**Now try again with proper numbers and you'll see the metrics display correctly!** 🚀 - YouTube Content Detection

## How to Test the System

The system is now properly configured to analyze YouTube videos and display likes, dislikes, and content verification!

### Test Steps:

1. **Open the application**: http://127.0.0.1:8000/

2. **Login** with your credentials

3. **Navigate to**: "Predict YouTube Content Type"

4. **Test Case 1 - With Manual Data Entry**:
   
   **Required Field:**
   - YouTube Video Link: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
   
   **Optional Fields (fill for complete analysis):**
   - Title: `Never Gonna Give You Up`
   - Channel Name: `Rick Astley`
   - Content Description: `Official music video for Never Gonna Give You Up`
   - Views: `1000000`
   - Likes: `50000`
   - Dislikes: `1000`
   - Comments: `25000`
   
   **Expected Result:**
   - ✅ **True Content** (safe, appropriate)
   - Shows all engagement metrics (views, likes, dislikes, comments)
   - Confidence Level: High

5. **Test Case 2 - Testing False Content Detection**:
   
   **Required Field:**
   - YouTube Video Link: `https://www.youtube.com/watch?v=test123`
   
   **Fill in:**
   - Title: `Violent Content Warning`
   - Content Description: `This video contains explicit violence and inappropriate content for children`
   - Views: `50000`
   - Likes: `100`
   - Dislikes: `5000`
   - Comments: `1000`
   
   **Expected Result:**
   - ⚠️ **False Content** (inappropriate detected)
   - Shows all engagement metrics
   - Confidence Level: High or Medium

6. **Test Case 3 - With Just Link (Minimal Input)**:
   
   **Required Field:**
   - YouTube Video Link: `https://www.youtube.com/watch?v=abc123xyz`
   
   Leave all other fields empty
   
   **Expected Result:**
   - ✅ **True Content** (default safe)
   - Shows default values (0 for metrics)
   - Note about manual data usage

## What You Should See:

### Results Page Shows:
1. ✅ or ⚠️ **Content Verification** (True/False)
2. **Video Information**:
   - Title
   - Channel Name
3. **Engagement Metrics** (color-coded cards):
   - 👁️ Views (Blue)
   - 👍 Likes (Green)
   - 👎 Dislikes (Red)
   - 💬 Comments (Orange)
4. **Confidence Level**
5. **Link to watch on YouTube**

## Important Notes:

### Current Behavior (Without YouTube API):
- You must **fill in the engagement metrics manually** (views, likes, dislikes, comments)
- System analyzes content based on keywords in title and description
- Works perfectly for manual testing

### With YouTube API (Optional Enhancement):
- Automatic data fetching from YouTube
- Just paste link and hit analyze
- No manual entry needed

To configure YouTube API, see: [YOUTUBE_API_SETUP.md](YOUTUBE_API_SETUP.md)

## Troubleshooting:

### Issue: No results showing
**Solution**: Make sure you clicked "Analyze Content with AI" button after entering the video link

### Issue: Shows "0" for all metrics
**Solution**: Fill in the engagement metrics fields manually (views, likes, dislikes, comments)

### Issue: Always shows "True Content"
**Solution**: Add inappropriate keywords in the title or content description to test false content detection (e.g., "violence", "explicit", "inappropriate")

## Keywords That Trigger False Content:
- violence, explicit, adult, inappropriate, harmful
- abuse, hate, racist, porn, drug, weapon
- kill, murder, blood, gore, nsfw, sexual
- terror, suicide, scam, fraud, fake

Use these in title or content description to test the detection system!

---

**Current Status**: ✅ System is working properly!
**Server**: Running at http://127.0.0.1:8000/
**Last Update**: January 10, 2026
