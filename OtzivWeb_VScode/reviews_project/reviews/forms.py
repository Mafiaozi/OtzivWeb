from django import forms
from .models import Review, Post

class PostForm(forms.ModelForm):
    display_name = forms.CharField(
        max_length=100,
        required=False,
        label="Отображаемое имя",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Post
        fields = ['name', 'text', 'display_name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Напишите ваш пост...',
                'class': 'form-control'
            })
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Оставьте ваш отзыв...',
                'class': 'form-control'
            })
        }