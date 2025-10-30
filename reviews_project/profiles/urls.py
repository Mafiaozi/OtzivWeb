from django.urls import path
from .views import profile_view
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('profile/', login_required(profile_view), name='profile'),
]