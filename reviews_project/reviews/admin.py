from django.contrib import admin
from .models import Post, Review

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'is_review', 'created_at')
    list_filter = ('is_review', 'created_at', 'user')
    search_fields = ('name', 'text', 'user__username')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('text', 'user__username', 'post__name')

