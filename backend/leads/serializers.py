from rest_framework import serializers
from .models import Lead, WebLink

class WebLinkSerializer(serializers.ModelSerializer):

    def __str__(self):
        return self.headline

    class Meta:
        model = WebLink
        fields = [ 'uri', 'job_lead' ]


class LeadSerializer(serializers.ModelSerializer):

    links = WebLinkSerializer(read_only=True, many=True)

    def __str__(self):
        return self.headline

    class Meta:
        model = Lead
        fields = [ 'id', 'company_name', 'median_salary', 'technology', 'created_on', 'contact_name', 'email', 
                   'description', 'notes', 'links' ]

    def create(self, validated_data):
        links_data = validated_data.pop('links')
        lead = Lead.objects.create(**validated_data)
        for link_data in links_data:
            WebLink.objects.create(job_lead=lead, **link_data)
        return musician

    def update(self, instance, validated_data):
        links_data = validated_data.pop('links')
        links = (instance.links).all()
        links = list(links)
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.median_salary = validated_data.get('median_salary', instance.median_salary)
        instance.technology = validated_data.get('technology', instance.technology)
        instance.contact_name = validated_data.get('contact_name', instance.contact_name)
        instance.email = validated_data.get('email', instance.email)
        instance.description = validated_data.get('description', instance.description)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.save()

        for link_data in links_data:
            link = links.pop(0)
            link.uri = link_data.get('uri', link.uri)
            link.save()
        return instance