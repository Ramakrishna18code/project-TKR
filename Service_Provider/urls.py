from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.serviceproviderlogin, name='serviceproviderlogin'),
    path('View_Remote_Users/', views.View_Remote_Users, name='View_Remote_Users'),
    path('View_Prediction_Of_YouTube_Content_Type/', views.View_Prediction_Of_YouTube_Content_Type, name='View_Prediction_Of_YouTube_Content_Type'),
    path('View_Prediction_Of_YouTube_Content_Ratio/', views.View_Prediction_Of_YouTube_Content_Ratio, name='View_Prediction_Of_YouTube_Content_Ratio'),
    path('charts/<str:chart_type>/', views.charts, name='charts'),
    path('charts1/<str:chart_type>/', views.charts1, name='charts1'),
    path('train_model/', views.train_model, name='train_model'),
]
