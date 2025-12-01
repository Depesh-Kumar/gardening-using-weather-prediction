from django.urls import path
from . import views

app_name = 'gardening'

urlpatterns = [
    path('', views.gardening_home, name='home'),
    path('weather/', views.weather_forecast, name='weather_forecast'),
    path('tips/', views.gardening_tips, name='tips_list'),
    path('tips/<int:tip_id>/', views.gardening_tip_detail, name='tip_detail'),
]
