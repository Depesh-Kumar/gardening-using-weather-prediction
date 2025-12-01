from django.urls import path
from . import views

app_name = 'preferences'

urlpatterns = [
    path('', views.set_preferences, name='preference_form'),
]
