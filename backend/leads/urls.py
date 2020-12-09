from .views import LeadViewSet, WebLinkViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'leads', LeadViewSet)
router.register(r'links', WebLinkViewSet)

urlpatterns = [
    path('', include(router.urls))
]
