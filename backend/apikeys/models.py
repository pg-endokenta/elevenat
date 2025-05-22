# models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
import secrets

User = get_user_model()

class APIKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api_keys')
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=40, unique=True, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = secrets.token_hex(20)  # 40文字のランダムキー
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.user.username})"
