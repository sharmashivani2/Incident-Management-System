from rest_framework import serializers
from incident.models import *

class SignUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    
    
class IncidentSerializers(serializers.ModelSerializer):
    reporter_name = serializers.SerializerMethodField()
    
    class Meta:
        model = IncidentDetails
        fields = "__all__"
        
        
    def get_reporter_name(self, obj): 
        try:
            name = f"{obj.reporter_name.first_name} {obj.reporter_name.last_name}"
            return name
        except Exception as e:
            return str(e)

class IncidentCreateSerializers(serializers.ModelSerializer):
     class Meta:
        model = IncidentDetails
        fields = (
            'incident_number',
            'reporter_name',
            'reported_datetime',
            'incident_details',
            'priority',
            'incident_status',
        )