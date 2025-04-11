from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Post
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect




def review_list(request):
    posts = Post.objects.all().order_by('-created_at')

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')

        form = ReviewForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("review_list")
    else:
        form = ReviewForm()

    return render(request, "reviews/review_list.html", {
        "posts": posts,
        "form": form
    })


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('review_list')
    else:
        form = UserCreationForm()
    return render(request, 'reviews/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('review_list')
    else:
        form = AuthenticationForm()
    return render(request, 'reviews/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('review_list')

@login_required
def delete_review(request, pk):
    review = get_object_or_404(Post, pk=pk)
    if request.user == review.user:
        review.delete()
    return redirect('review_list')



