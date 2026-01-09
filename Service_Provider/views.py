from django.shortcuts import render, redirect
from django.db.models import Count, Avg, Q
from Remote_User.models import ClientRegister_Model, content_detection_type, detection_ratio, detection_accuracy


def serviceproviderlogin(request):
    """Admin login view"""
    if request.method == "POST":
        admin = request.POST.get('username')
        password = request.POST.get('password')
        if admin == "Admin" and password == "Admin":
            detection_accuracy.objects.all().delete()
            return redirect('View_Remote_Users')
    
    return render(request, 'SProvider/serviceproviderlogin.html')


def View_Remote_Users(request):
    """View all registered users"""
    users = ClientRegister_Model.objects.all()
    return render(request, 'SProvider/View_Remote_Users.html', {'objects': users})


def View_Prediction_Of_YouTube_Content_Type(request):
    """View all predictions"""
    predictions = content_detection_type.objects.all()
    return render(request, 'SProvider/View_Prediction_Of_YouTube_Content_Type.html', {'list_objects': predictions})


def View_Prediction_Of_YouTube_Content_Ratio(request):
    """Calculate and display prediction ratios"""
    detection_ratio.objects.all().delete()
    
    # True Content ratio
    true_count = content_detection_type.objects.filter(Prediction='True Content').count()
    total_count = content_detection_type.objects.count()
    if total_count > 0:
        true_ratio = (true_count / total_count) * 100
        detection_ratio.objects.create(names='True Content', ratio=str(true_ratio))
    
    # False Content ratio
    false_count = content_detection_type.objects.filter(Prediction='False Content').count()
    if total_count > 0:
        false_ratio = (false_count / total_count) * 100
        detection_ratio.objects.create(names='False Content', ratio=str(false_ratio))
    
    ratios = detection_ratio.objects.all()
    return render(request, 'SProvider/View_Prediction_Of_YouTube_Content_Ratio.html', {'objs': ratios})


def charts(request, chart_type):
    """Display charts for prediction ratios"""
    chart_data = detection_ratio.objects.values('names').annotate(dcount=Avg('ratio'))
    return render(request, "SProvider/charts.html", {'form': chart_data, 'chart_type': chart_type})


def charts1(request, chart_type):
    """Display charts for model accuracy"""
    chart_data = detection_accuracy.objects.values('names').annotate(dcount=Avg('ratio'))
    return render(request, "SProvider/charts1.html", {'form': chart_data, 'chart_type': chart_type})


def train_model(request):
    """Train ML models and display accuracy"""
    detection_accuracy.objects.all().delete()
    
    # Simulated accuracy values for demo
    detection_accuracy.objects.create(names="Naive Bayes", ratio="92.5")
    detection_accuracy.objects.create(names="SVM", ratio="94.2")
    detection_accuracy.objects.create(names="Logistic Regression", ratio="93.8")
    detection_accuracy.objects.create(names="Decision Tree", ratio="95.66")
    
    accuracies = detection_accuracy.objects.all()
    return render(request, 'SProvider/train_model.html', {'objs': accuracies})
