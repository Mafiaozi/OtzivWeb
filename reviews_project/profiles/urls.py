from django.urls import path

from .views import delete_avatar, profile_view

urlpatterns = [
    path('', profile_view, name='profile'),
    path('delete-avatar/', delete_avatar, name='delete_avatar'),
]
