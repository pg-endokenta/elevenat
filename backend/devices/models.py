from django.db import models
import uuid

from django.contrib.auth import get_user_model

User = get_user_model()

class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='devices')
    name = models.CharField(max_length=255)
    mac_address = models.CharField(max_length=17, unique=True)

    def __str__(self):
        return f"{self.user.username}: {self.name} ({self.mac_address})"