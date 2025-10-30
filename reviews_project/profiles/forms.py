from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date', 'avatar']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }
        error_messages = {
            'birth_date': {
                'invalid': 'Пожалуйста, введите корректную дату в формате ДД.ММ.ГГГГ',
            },
        }