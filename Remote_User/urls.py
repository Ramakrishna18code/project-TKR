from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('Register1/', views.Register1, name='Register1'),
    path('ViewYourProfile/', views.ViewYourProfile, name='ViewYourProfile'),
    path('Predict_YouTube_Content_Type/', views.Predict_YouTube_Content_Type, name='Predict_YouTube_Content_Type'),
]
