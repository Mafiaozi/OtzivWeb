from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

# Сигнал для создания профиля при создании пользователя
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Проверка, существует ли профиль для этого пользователя
        if not Profile.objects.filter(user=instance).exists():
            Profile.objects.create(user=instance)

# Сигнал для сохранения профиля при изменении пользователя
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Проверка, существует ли профиль у пользователя
    if hasattr(instance, 'profile'):
        instance.profile.save()
