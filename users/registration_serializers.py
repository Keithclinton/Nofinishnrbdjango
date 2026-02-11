from rest_framework import serializers
from .models import IndividualRegistration

class IndividualRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualRegistration
        fields = '__all__'
        read_only_fields = ('user', 'created_at')
