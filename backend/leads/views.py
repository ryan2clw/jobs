from django.shortcuts import render
from .models import Lead, WebLink
from .serializers import LeadSerializer
from rest_framework import viewsets

# Create your views here.
class LeadViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing job leads.
    """
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()

class WebLinkViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = LeadSerializer
    queryset = WebLink.objects.all()