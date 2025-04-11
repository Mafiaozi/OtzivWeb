from django import forms
from .models import Post

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }