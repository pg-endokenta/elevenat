from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import APIKey

@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'key', 'is_active', 'created_at')
    readonly_fields = ('key',)