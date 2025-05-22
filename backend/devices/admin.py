from django.contrib import admin

# Register your models here.

from .models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'mac_address')
