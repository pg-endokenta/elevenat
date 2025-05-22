from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class MacListSerializer(serializers.Serializer):
    mac_addresses = serializers.ListField(
        child=serializers.CharField(max_length=17),
        allow_empty=False
    )


class PresenceStatsSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    username = serializers.CharField()
    last_seen = serializers.DateTimeField(allow_null=True)
    total_count = serializers.IntegerField()
    today_count = serializers.IntegerField()