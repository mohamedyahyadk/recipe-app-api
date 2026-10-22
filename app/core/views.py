"""
Core views for the application.
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response    


@api_view(['GET'])
def health_check(request):
    """
    Health check endpoint to verify the API is running.

    Returns a JSON response with a status message.
    """
    return Response({'status': 'ok'})