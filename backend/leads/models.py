""" Generates SQL tables for Leads """
from django.db import models

class Lead(models.Model):
    """ A basic job lead 
            fields = [ 'id', 'company_name', 'median_salary', 'technology', 'created_on', 'contact_name', 'email', 
                   'description', 'notes' ]
    
    """
    created_on = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(max_length=100)
    median_salary=models.IntegerField(null=True)
    technology = models.CharField(max_length=500, null=True)
    contact_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    description = models.TextField() # Where and what industry
    notes = models.TextField(null=True)

    def __str__(self):
        return str(self.description) + ", uses: " + str(self.technology)

class WebLink(models.Model):
    """ Links to the job description """
    uri = models.CharField(max_length=100)
    job_lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='links')
