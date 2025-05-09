from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from .models import Review, Post
from .forms import ReviewForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


@login_required
def review_list(request):
    reviews = Post.objects.filter(is_review=True).select_related('user').order_by('-created_at')

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            post = Post.objects.create(
                name=f"Отзыв от {request.user.username}",
                text=form.cleaned_data['text'],
                user=request.user,
                is_review=True
            )
            messages.success(request, 'Отзыв успешно добавлен!')
            return redirect('review_list')
    else:
        form = ReviewForm()

    return render(request, "reviews/review_list.html", {
        "reviews": reviews,
        "form": form
    })


@require_POST
@login_required
def delete_review(request, pk):
    review = get_object_or_404(Post, pk=pk, is_review=True)
    if request.user == review.user or request.user.is_superuser:
        review.delete()
        messages.success(request, 'Отзыв удален')
    else:
        messages.error(request, 'У вас нет прав для удаления этого отзыва')
    return redirect('review_list')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('review_list')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('review_list')
    else:
        form = UserCreationForm()

    return render(request, 'reviews/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('review_list')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.username}!')
            return redirect('review_list')
        messages.error(request, 'Неверное имя пользователя или пароль')
    else:
        form = AuthenticationForm()

    return render(request, 'reviews/login.html', {'form': form})

@login_required
@require_POST
def logout_view(request):
    logout(request)
    messages.info(request, 'Вы вышли из системы.')
    return redirect('review_list')


def delete_review(request, pk):
    review = get_object_or_404(Post, pk=pk, is_review=True)

    if not (request.user == review.user or request.user.is_superuser):
        messages.error(request, 'У вас нет прав для этого действия.')
        return redirect('review_list')

    review.delete()
    messages.success(request, 'Отзыв успешно удален.')
    return redirect('review_list')

@login_required
def profile_view(request):
    user_posts = Post.objects.filter(user=request.user).order_by('-created_at')
    user_reviews = Review.objects.filter(user=request.user).select_related('post').order_by('-created_at')

    # Пагинация для постов
    post_paginator = Paginator(user_posts, 5)
    post_page = request.GET.get('post_page')
    posts_page_obj = post_paginator.get_page(post_page)

    # Пагинация для отзывов
    review_paginator = Paginator(user_reviews, 5)
    review_page = request.GET.get('review_page')
    reviews_page_obj = review_paginator.get_page(review_page)

    context = {
        'posts_page_obj': posts_page_obj,
        'reviews_page_obj': reviews_page_obj,
        'user': request.user
    }
    return render(request, 'reviews/profile.html', context)


class ReviewListAPIView(APIView):
    """
    API для работы с отзывами
    """
    permission_classes = [IsAuthenticatedOrReadOnly]  # Добавьте permissions

    def get(self, request):
        reviews = Review.objects.select_related('user', 'post').all()
        serializer = ReviewSerializer(reviews, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            # Автоматически устанавливаем пользователя из запроса
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def post_list(request):
    # Правильные запросы с использованием is_review
    reviews = Post.objects.filter(is_review=True).order_by('-created_at')
    regular_posts = Post.objects.filter(is_review=False).order_by('-created_at')

    context = {
        'reviews': reviews,
        'regular_posts': regular_posts
    }
    return render(request, 'reviews/review_list.html', context)