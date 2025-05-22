from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, timezone as dt_timezone 
from apikeys.authentication import APIKeyAuthentication
from .serializers import MacListSerializer
from .models import Device, PresenceDetection
from rest_framework import status

from django.db.models.functions import TruncMinute




from django.db.models import Max
from django.contrib.auth import get_user_model
from .serializers import PresenceStatsSerializer

User = get_user_model()

# Create your views here.


class LogNowView(APIView):
    """
    View to return the last seen time (in minutes ago) for each user.
    """

    def post(self, request, *args, **kwargs):
        now = timezone.now()

        # userごとに最新のPresenceDetectionを取得（PostgreSQLのみ対応）
        latest_detections = (
            PresenceDetection.objects
            .order_by('user_id', '-detected_at')  # userごとに最新の検出を得るためにソート
            .distinct('user_id')
            .select_related('user')
        )

        data = []
        for idx, detection in enumerate(latest_detections):
            minutes = int((now - detection.detected_at).total_seconds() // 60)
            data.append({
                "id": str(idx),
                "name": detection.user.username,
                "last_seen": minutes
            })

        return Response(data, status=200)




class PresenceDetectionView(APIView):
    authentication_classes = [APIKeyAuthentication]
    permission_classes = []  # 必要に応じて IsAuthenticated も追加可能

    def post(self, request):
        serializer = MacListSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        mac_list = serializer.validated_data['mac_addresses']
        now = timezone.now().replace(second=0, microsecond=0)

        matched_devices = Device.objects.filter(mac_address__in=mac_list).select_related('user')

        detections = [
            PresenceDetection(user=device.user, device=device, detected_at=now)
            for device in matched_devices
        ]

        PresenceDetection.objects.bulk_create(detections, ignore_conflicts=True)

        return Response({
            "detected_users": [device.user.username for device in matched_devices],
            "count": len(matched_devices),
        }, status=status.HTTP_201_CREATED)


class PresenceStatsView(APIView):
    def get(self, request):
        now = timezone.now()
        today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)

        # 1分単位に丸めたうえで、(user, minute) 単位の出現を集計
        minute_level = (
            PresenceDetection.objects
            .annotate(minute=TruncMinute('detected_at'))
            .values('user_id', 'minute')
            .order_by()
        )

        # ユーザーごとの、ユニークな minute 出現数と最終検出時間を取得
        summary = {}

        for entry in minute_level:
            user_id = entry['user_id']
            minute = entry['minute']
            if user_id not in summary:
                summary[user_id] = {
                    'total_count': 0,
                    'today_count': 0,
                    'last_seen': minute,
                }
            summary[user_id]['total_count'] += 1
            if minute >= today_start:
                summary[user_id]['today_count'] += 1
            if minute > summary[user_id]['last_seen']:
                summary[user_id]['last_seen'] = minute

        # 全ユーザー分データ生成
        users = User.objects.all()
        data = []

        for user in users:
            s = summary.get(user.id, {})
            data.append({
                "user_id": user.id,
                "username": user.username,
                "last_seen": s.get("last_seen"),
                "total_count": s.get("total_count", 0),
                "today_count": s.get("today_count", 0),
            })

        # 最新検出順に並べ替え
        data.sort(
            key=lambda d: d["last_seen"] or datetime.min.replace(tzinfo=dt_timezone.utc),
            reverse=True,
        )

        serializer = PresenceStatsSerializer(data, many=True)
        return Response(serializer.data)