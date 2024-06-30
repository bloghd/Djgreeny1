from django.urls import path
from .views import register, user_activate, profile

app_name = 'accounts'

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('<str:username>/activate', user_activate , name='user_activate'),
]
