from django.contrib.auth import views as auth_views
from django.urls import path
from .views import review_list, register_view, login_view, logout_view, delete_review
from .views import ReviewListAPIView

urlpatterns = [
    path('', review_list, name='review_list'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('delete/<int:pk>/', delete_review, name='delete_review'),
    path('api/reviews/', ReviewListAPIView.as_view(), name='api_reviews'),
]