""" Generates SQL tables for Leads """
from django.db import models

class Lead(models.Model):
    """ A basic job lead """
    created_on = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    notes = models.TextField()

    def __str__(self):
        return str(self.company_name) + ", " + str(self.description)