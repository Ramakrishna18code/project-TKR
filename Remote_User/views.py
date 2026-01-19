from django.shortcuts import render, redirect
from django.db.models import Q
from .models import ClientRegister_Model, content_detection_type
from Service_Provider.models import detection_ratio, detection_accuracy
from .forms import ClientRegister_Form
import re
from datetime import datetime
import os
import sys

# Add parent directory to path to import config
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Lazy import heavy libraries only when needed
def lazy_import_ml_libs():
    """Import heavy ML libraries only when needed to save memory"""
    import pandas as pd
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import MultinomialNB
    from sklearn import svm
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.ensemble import VotingClassifier
    return pd, CountVectorizer, train_test_split, MultinomialNB, svm, LogisticRegression, DecisionTreeClassifier, VotingClassifier

def lazy_import_youtube_api():
    """Import YouTube API only when needed"""
    from googleapiclient.discovery import build
    return build


def index(request):
    """Homepage view"""
    return render(request, 'RUser/index.html')


def login(request):
    """User login view"""
    error_message = None
    if request.method == "POST" and 'submit1' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            error_message = 'Please enter both username and password'
        else:
            try:
                user = ClientRegister_Model.objects.get(username=username, password=password)
                request.session["userid"] = user.id
                return redirect('ViewYourProfile')
            except ClientRegister_Model.DoesNotExist:
                error_message = 'Invalid username or password. Please try again or register first.'
    
    return render(request, 'RUser/login.html', {'error': error_message})


def Register1(request):
    """User registration view"""
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phoneno = request.POST.get('phoneno')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        
        ClientRegister_Model.objects.create(
            username=username, email=email, password=password, phoneno=phoneno,
            country=country, state=state, city=city, address=address, gender=gender
        )
        
        return render(request, 'RUser/Register1.html', {'object': 'Registered Successfully'})
    
    return render(request, 'RUser/Register1.html')


def ViewYourProfile(request):
    """View user profile"""
    userid = request.session.get('userid')
    if not userid:
        return redirect('login')
    
    user = ClientRegister_Model.objects.get(id=userid)
    return render(request, 'RUser/ViewYourProfile.html', {'object': user})


def extract_video_id(url):
    """Extract video ID from YouTube URL"""
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',
        r'(?:embed\/|v\/|youtu.be\/)([0-9A-Za-z_-]{11})'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return url


def get_youtube_video_data(video_id):
    """Fetch video data from YouTube API"""
    try:
        # Try to import API key and demo mode from config
        try:
            from config import YOUTUBE_API_KEY, DEMO_MODE
            API_KEY = YOUTUBE_API_KEY
            demo_mode = DEMO_MODE
            print(f"Config loaded - API Key: {API_KEY[:20]}..., Demo Mode: {demo_mode}")
        except Exception as e:
            print(f"Config import error: {e}")
            API_KEY = 'YOUR_YOUTUBE_API_KEY_HERE'
            demo_mode = False
        
        # If API key is not set but demo mode is enabled, return demo data
        if (not API_KEY or API_KEY == 'YOUR_YOUTUBE_API_KEY_HERE') and demo_mode:
            print("Demo Mode: Returning sample data")
            # Return realistic demo data
            return {
                'title': 'Sample Educational Video for Kids',
                'channel_title': 'Learning Channel',
                'description': 'This is a wonderful educational video teaching children about science, math, and creativity. Perfect for kids aged 5-12. Family-friendly content with fun animations and engaging lessons.',
                'category': '27',  # Education category
                'publish_date': '2024-01-15T10:00:00Z',
                'views': '1234567',
                'likes': '98765',
                'dislikes': '123',
                'comment_count': '5432',
            }
        
        # If API key is not set and not demo mode, return None
        if not API_KEY or API_KEY == 'YOUR_YOUTUBE_API_KEY_HERE':
            print("YouTube API Key not configured. Please set it in config.py")
            return None
        
        # Make API call with real key
        print(f"Fetching data for video ID: {video_id}")
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        
        request = youtube.videos().list(
            part='snippet,statistics,contentDetails',
            id=video_id
        )
        response = request.execute()
        
        print(f"API Response: {len(response.get('items', []))} items found")
        
        if response['items']:
            video = response['items'][0]
            snippet = video['snippet']
            statistics = video['statistics']
            
            data = {
                'title': snippet.get('title', ''),
                'channel_title': snippet.get('channelTitle', ''),
                'description': snippet.get('description', ''),
                'category': snippet.get('categoryId', ''),
                'publish_date': snippet.get('publishedAt', ''),
                'views': statistics.get('viewCount', '0'),
                'likes': statistics.get('likeCount', '0'),
                'dislikes': statistics.get('dislikeCount', '0'),
                'comment_count': statistics.get('commentCount', '0'),
            }
            print(f"Fetched: {data['title']}, Views: {data['views']}, Likes: {data['likes']}")
            return data
    except Exception as e:
        print(f"YouTube API Error: {e}")
        import traceback
        traceback.print_exc()
    
    return None


def Predict_YouTube_Content_Type(request):
    """Predict content type using ML models and YouTube API"""
    # Handle AJAX requests for fetching YouTube data
    if request.method == "GET" and request.GET.get('fetch_data'):
        from django.http import JsonResponse
        video_link = request.GET.get('video_link', '').strip()
        if video_link:
            video_id = extract_video_id(video_link)
            youtube_data = get_youtube_video_data(video_id)
            if youtube_data:
                # Check if demo mode
                try:
                    from config import DEMO_MODE
                    is_demo = DEMO_MODE
                except:
                    is_demo = False
                    
                return JsonResponse({
                    'success': True,
                    'data': youtube_data,
                    'demo_mode': is_demo
                })
        return JsonResponse({'success': False, 'message': 'API not configured. Please enter data manually or enable DEMO_MODE in config.py'})
    
    if request.method == "POST":
        Video_link = request.POST.get('Video_link', '').strip()
        
        if not Video_link:
            return render(request, 'RUser/Predict_YouTube_Content_Type.html', {
                'error': 'Please provide a YouTube video link'
            })
        
        # Extract video ID from URL
        video_id = extract_video_id(Video_link)
        
        # Try to fetch data from YouTube API
        youtube_data = get_youtube_video_data(video_id)
        
        # Initialize variables
        api_used = False
        
        if youtube_data:
            # Use YouTube API data
            api_used = True
            title = youtube_data['title']
            channel_title = youtube_data['channel_title']
            content = youtube_data['description']
            views = youtube_data['views']
            likes = youtube_data['likes']
            dislikes = youtube_data['dislikes']
            comment_count = youtube_data['comment_count']
            category = youtube_data['category']
            publish_date = youtube_data['publish_date']
            publish_time = ''
            views_per_day = '0'
        else:
            # Fallback to manual input - prioritize API data if available in POST
            video_id = request.POST.get('video_id', video_id)
            title = request.POST.get('title', '').strip()
            channel_title = request.POST.get('channel_title', '').strip()
            category = request.POST.get('category', '').strip()
            publish_time = request.POST.get('publish_time', '')
            content = request.POST.get('content', '').strip()
            views = request.POST.get('views', '0').strip()
            likes = request.POST.get('likes', '0').strip()
            dislikes = request.POST.get('dislikes', '0').strip()
            comment_count = request.POST.get('comment_count', '0').strip()
            publish_date = request.POST.get('publish_date', '')
            views_per_day = request.POST.get('views_per_day', '0').strip()
            
            # If fields are empty, try to fetch again
            if not title or not content:
                temp_data = get_youtube_video_data(video_id)
                if temp_data:
                    api_used = True
                    title = title or temp_data['title']
                    channel_title = channel_title or temp_data['channel_title']
                    content = content or temp_data['description']
                    views = views if views != '0' else temp_data['views']
                    likes = likes if likes != '0' else temp_data['likes']
                    dislikes = dislikes if dislikes != '0' else temp_data['dislikes']
                    comment_count = comment_count if comment_count != '0' else temp_data['comment_count']
                    category = category or temp_data['category']
                    publish_date = publish_date or temp_data['publish_date']
            
            # If no content provided, use title and video link for basic analysis
            if not content and not title:
                content = f"Video analysis for: {Video_link}"
                title = "YouTube Video Analysis"

        # Enhanced Content verification logic with weighted categories
        
        # High-risk keywords (weight: 3) - Strong indicators of inappropriate content
        high_risk_keywords = [
            'porn', 'pornography', 'xxx', 'sex', 'sexual', 'nude', 'naked', 'nsfw',
            'violence', 'violent', 'kill', 'murder', 'death', 'blood', 'gore', 'brutal',
            'drug', 'cocaine', 'heroin', 'marijuana', 'weed', 'meth',
            'suicide', 'self-harm', 'cutting',
            'hate', 'racist', 'terrorism', 'terror', 'extremist'
        ]
        
        # Medium-risk keywords (weight: 2) - Context-dependent
        medium_risk_keywords = [
            'weapon', 'gun', 'knife', 'bomb', 'explosive',
            'abuse', 'assault', 'attack', 'fight', 'fighting',
            'alcohol', 'drunk', 'beer', 'vodka',
            'gambling', 'casino', 'betting',
            'scary', 'horror', 'disturbing'
        ]
        
        # Low-risk keywords (weight: 1) - May be inappropriate in certain contexts
        low_risk_keywords = [
            'explicit', 'inappropriate', 'adult', 'mature',
            'dangerous', 'harmful', 'toxic', 'controversy',
            'scam', 'fraud', 'fake', 'misleading',
            'graphic', 'intense'
        ]
        
        # Positive/Safe keywords (bonus points) - Indicates safe content
        safe_keywords = [
            'educational', 'learning', 'tutorial', 'kids', 'children', 'family',
            'wholesome', 'friendly', 'safe', 'appropriate', 'cartoon', 'animation',
            'science', 'math', 'reading', 'lesson', 'school', 'teach'
        ]
        
        # Check content and title
        content_lower = content.lower() if content else ''
        title_lower = title.lower() if title else ''
        combined_text = content_lower + ' ' + title_lower
        
        # Calculate risk score with weighted keywords
        risk_score = 0
        found_keywords = []
        
        # Check high-risk keywords (weight: 3)
        for keyword in high_risk_keywords:
            if keyword in combined_text:
                risk_score += 3
                found_keywords.append(f"{keyword} (High Risk)")
        
        # Check medium-risk keywords (weight: 2)
        for keyword in medium_risk_keywords:
            if keyword in combined_text:
                risk_score += 2
                found_keywords.append(f"{keyword} (Medium Risk)")
        
        # Check low-risk keywords (weight: 1)
        for keyword in low_risk_keywords:
            if keyword in combined_text:
                risk_score += 1
                found_keywords.append(f"{keyword} (Low Risk)")
        
        # Check safe keywords (reduce risk score)
        safe_count = sum(1 for keyword in safe_keywords if keyword in combined_text)
        risk_score -= safe_count  # Reduce risk for educational/safe content
        
        # Log detection details
        if found_keywords:
            print(f"Risk Analysis - Score: {risk_score}, Keywords found: {', '.join(found_keywords[:5])}")
        
        # Determine if content is true or false based on risk score
        if risk_score >= 5:
            val = 'False Content'
            confidence = 'Very High'
            reason = f"Detected {len(found_keywords)} inappropriate indicators (Risk Score: {risk_score})"
        elif risk_score >= 3:
            val = 'False Content'
            confidence = 'High'
            reason = f"Multiple inappropriate keywords found (Risk Score: {risk_score})"
        elif risk_score >= 1:
            val = 'False Content'
            confidence = 'Medium'
            reason = f"Potentially inappropriate content detected (Risk Score: {risk_score})"
        elif risk_score <= -2:
            val = 'True Content'
            confidence = 'Very High'
            reason = f"Strong educational/safe content indicators (Safe Score: {abs(risk_score)})"
        else:
            val = 'True Content'
            confidence = 'High'
            reason = "No inappropriate content detected"

        # Ensure numeric values - handle both string and int inputs
        try:
            # Convert to int first, then back to string for consistency
            views = str(int(float(views))) if views and str(views).replace('.', '').replace('-', '').isdigit() else '0'
        except (ValueError, AttributeError):
            views = '0'
            
        try:
            likes = str(int(float(likes))) if likes and str(likes).replace('.', '').replace('-', '').isdigit() else '0'
        except (ValueError, AttributeError):
            likes = '0'
            
        try:
            dislikes = str(int(float(dislikes))) if dislikes and str(dislikes).replace('.', '').replace('-', '').isdigit() else '0'
        except (ValueError, AttributeError):
            dislikes = '0'
            
        try:
            comment_count = str(int(float(comment_count))) if comment_count and str(comment_count).replace('.', '').replace('-', '').isdigit() else '0'
        except (ValueError, AttributeError):
            comment_count = '0'
        
        # Debug: Print values to check
        print(f"DEBUG - Views: {views}, Likes: {likes}, Dislikes: {dislikes}, Comments: {comment_count}")

        # Save to database
        content_detection_type.objects.create(
            video_id=video_id,
            title=title or 'YouTube Video',
            channel_title=channel_title or 'Unknown Channel',
            category=category or 'General',
            publish_time=publish_time,
            content=content or 'No description available',
            views=views,
            likes=likes,
            dislikes=dislikes,
            comment_count=comment_count,
            Video_link=Video_link,
            publish_date=publish_date,
            views_per_day=views_per_day,
            Prediction=val
        )

        context = {
            'objs': val,
            'video_data': {
                'title': title or 'YouTube Video',
                'channel': channel_title or 'Unknown Channel',
                'likes': likes,
                'dislikes': dislikes,
                'views': views,
                'comments': comment_count,
                'video_link': Video_link,
                'confidence': confidence,
                'api_used': api_used,
                'reason': reason,
                'keywords_found': len(found_keywords),
                'risk_score': risk_score
            }
        }
        
        return render(request, 'RUser/Predict_YouTube_Content_Type.html', context)
    
    return render(request, 'RUser/Predict_YouTube_Content_Type.html')
