from rest_framework import serializers
from .models import Lead, WebLink
""" Main ViewSets """
class WebLinkSerializer(serializers.ModelSerializer):

    def __str__(self):
        return self.uri

    class Meta:
        model = WebLink
        fields = [ 'uri', 'job_lead' ]
        

        
""" ListView """
class WebLinkListSerializer(serializers.ModelSerializer):

    def __str__(self):
        return self.uri

    class Meta:
        model = WebLink
        fields = [ 'uri' ]

    def to_representation(self, instance):
        return instance.uri


class LeadSerializer(serializers.HyperlinkedModelSerializer):

    links = WebLinkListSerializer(read_only=True, many=True)
    edit = serializers.HyperlinkedIdentityField(view_name='lead-detail', format='html')

    def __str__(self):
        return self.headline

    class Meta:
        model = Lead
        fields = [ 'id', 'edit', 'company_name', 'median_salary', 'technology', 'created_on', 'contact_name', 'email', 
                   'description', 'notes', 'links' ]

    # def create(self, validated_data):
    #     links_data = validated_data.pop('links')
    #     lead = Lead.objects.create(**validated_data)
    #     for link_data in links_data:
    #         WebLink.objects.create(job_lead=lead, **link_data)
    #     return lead

    # def update(self, instance, validated_data):
    #     links_data = validated_data.pop('links')
    #     links = (instance.links).all()
    #     instance.company_name = validated_data.get('company_name', instance.company_name)
    #     instance.median_salary = validated_data.get('median_salary', instance.median_salary)
    #     instance.technology = validated_data.get('technology', instance.technology)
    #     instance.contact_name = validated_data.get('contact_name', instance.contact_name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.notes = validated_data.get('notes', instance.notes)
    #     instance.save()

    #     for links in links_data:
    #         link = links.pop(0)
    #         link.uri = link_data.get('uri', link.uri)
    #         link.job_lead = link_data.get('job_lead', link.job_lead)
    #         link.save()
    #     return instance