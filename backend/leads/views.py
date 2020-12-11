from django.shortcuts import render
from .models import Lead, WebLink
from .serializers import LeadSerializer, WebLinkSerializer
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
    A viewset for viewing and editing links to jobs.
    """
    serializer_class = WebLinkSerializer
    queryset = WebLink.objects.all()