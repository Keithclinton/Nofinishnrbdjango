from rest_framework import serializers
from .blog_models import BlogPost, ImpactStory, Clinic, ChallengeEntry

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

class ImpactStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpactStory
        fields = '__all__'

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = '__all__'

class ChallengeEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallengeEntry
        fields = '__all__'
