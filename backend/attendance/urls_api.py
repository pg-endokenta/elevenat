# urls.py

from django.urls import path
from .views import PresenceDetectionView, PresenceStatsView

urlpatterns = [
    path('detect/', PresenceDetectionView.as_view(), name='presence-detect'),
    path('presence-stats/', PresenceStatsView.as_view(), name='presence-stats-api'),
]
