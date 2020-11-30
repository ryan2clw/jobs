from .views import LeadViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'leads', LeadViewSet)

urlpatterns = [
    path('', include(router.urls))
]
