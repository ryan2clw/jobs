from rest_framework import serializers
from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['id','company_name', 'contact_name', 'email', 'description', 'notes']