from django.contrib import admin


from .models import PresenceDetection

@admin.register(PresenceDetection)
class PresenceDetectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'device', 'detected_at')
