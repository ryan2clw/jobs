from django.contrib import admin
from .models import Lead


class LeadAdmin(admin.ModelAdmin):
    fields = ['company_name', 'median_salary', 'technology', 'contact_name', 'email', 
                   'description', 'notes', 'links']

admin.site.register(Lead, LeadAdmin)