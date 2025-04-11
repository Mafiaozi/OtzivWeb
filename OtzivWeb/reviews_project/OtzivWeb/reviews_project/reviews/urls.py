from django.urls import path
from .views import review_list, register_view, login_view, logout_view, delete_review

urlpatterns = [
    path('', review_list, name='review_list'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('delete/<int:pk>/', delete_review, name='delete_review'),
]