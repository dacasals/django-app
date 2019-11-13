# views.py
from rest_framework import viewsets
from .serializers import TreeSerializer
from .models import Topic
from rest_framework.permissions import AllowAny


class TreeViewSet(viewsets.ReadOnlyModelViewSet):
    """
        A simple ViewSet for viewing and editing accounts.
    """
    queryset = Topic.objects.all().filter(show_in_home=True)
    serializer_class =  TreeSerializer
    permission_classes = [AllowAny]


