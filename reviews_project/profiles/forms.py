from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    birth_date = forms.DateField(
        required=False,
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        error_messages={
            'invalid': 'Пожалуйста, введите корректную дату.',
        },
    )

    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date', 'avatar']
        widgets = {
            'avatar': forms.FileInput(attrs={'accept': 'image/*'}),
        }
