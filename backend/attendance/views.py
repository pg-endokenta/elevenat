from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class LogNowView(APIView):
    """
    View to log the current time.
    """

    def post(self, request, *args, **kwargs):
        """
        Handle GET requests to log the current time.
        """
        
        data = [
            {
                "id": "0",
                "name": "遠",
                "last_seen": 40
            },
            {
                "id": "1",
                "name": "藤",
                "last_seen": 80
            },
            {
                "id": "2",
                "name": "健",
                "last_seen": 160
            },
            {
                "id": "3",
                "name": "太",
                "last_seen": 320
            },
        ]


        # Return a response
        return Response(data, status=200)
