from rest_framework import serializers
from .volunteer_models import VolunteerApplication

class VolunteerApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerApplication
        fields = '__all__'
        read_only_fields = ('submitted_at',)
