from django.db import models
import uuid

from devices.models import Device

from django.utils import timezone




from django.contrib.auth import get_user_model

User = get_user_model()

class PresenceDetection(models.Model):
    """
    Model to store presence detection data.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='presence_detections')
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='presence_detections')
    detected_at = models.DateTimeField(default=timezone.now)
