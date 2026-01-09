from django.shortcuts import render, redirect
from django.db.models import Q
from .models import ClientRegister_Model, content_detection_type
from .forms import ClientRegister_Form
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier


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


def Predict_YouTube_Content_Type(request):
    """Predict content type using ML models"""
    if request.method == "POST":
        video_id = request.POST.get('video_id', '')
        title = request.POST.get('title', '')
        channel_title = request.POST.get('channel_title', '')
        category = request.POST.get('category', '')
        publish_time = request.POST.get('publish_time', '')
        content = request.POST.get('content', '')
        views = request.POST.get('views', '0')
        likes = request.POST.get('likes', '0')
        dislikes = request.POST.get('dislikes', '0')
        comment_count = request.POST.get('comment_count', '0')
        Video_link = request.POST.get('Video_link', '')
        publish_date = request.POST.get('publish_date', '')
        views_per_day = request.POST.get('views_per_day', '0')

        # Simple prediction logic (placeholder - replace with actual model)
        # For demo purposes, using keyword-based classification
        inappropriate_keywords = ['violence', 'explicit', 'adult', 'inappropriate', 'harmful']
        val = 'False Content' if any(keyword in content.lower() for keyword in inappropriate_keywords) else 'True Content'

        content_detection_type.objects.create(
            video_id=video_id,
            title=title,
            channel_title=channel_title,
            category=category,
            publish_time=publish_time,
            content=content,
            views=views,
            likes=likes,
            dislikes=dislikes,
            comment_count=comment_count,
            Video_link=Video_link,
            publish_date=publish_date,
            views_per_day=views_per_day,
            Prediction=val
        )

        return render(request, 'RUser/Predict_YouTube_Content_Type.html', {'objs': val})
    
    return render(request, 'RUser/Predict_YouTube_Content_Type.html')
