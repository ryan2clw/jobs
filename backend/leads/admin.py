from django.contrib import admin
from .models import Lead


class LeadAdmin(admin.ModelAdmin):
    fields = ['company_name', 'contact_name', 'email', 'description', 'notes']

admin.site.register(Lead, LeadAdmin)