from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('reviews.urls')),  # Все auth URLs
    path('profile/', include('profiles.urls')),  # Профиль
    path('', include('reviews.urls')),  # Главная страница
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)