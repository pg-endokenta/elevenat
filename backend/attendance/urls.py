from django.urls import path
from attendance.views import LogNowView

urlpatterns = [
    path("logs/now/", LogNowView.as_view(), name="log_now"),
]
