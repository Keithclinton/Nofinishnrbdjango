from rest_framework import generics, status, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .blog_models import BlogPost, ImpactStory, Clinic, ChallengeEntry
from .blog_serializers import BlogPostSerializer, ImpactStorySerializer, ClinicSerializer, ChallengeEntrySerializer

class BlogPostListView(generics.ListAPIView):
    queryset = BlogPost.objects.all().order_by('-created_at')
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]

class ImpactStoryListView(generics.ListAPIView):
    queryset = ImpactStory.objects.all().order_by('-created_at')
    serializer_class = ImpactStorySerializer
    permission_classes = [permissions.AllowAny]

class ClinicListView(generics.ListAPIView):
    queryset = Clinic.objects.all().order_by('-start_date')
    serializer_class = ClinicSerializer
    permission_classes = [permissions.AllowAny]

class ChallengeEntryCreateView(generics.CreateAPIView):
    queryset = ChallengeEntry.objects.all()
    serializer_class = ChallengeEntrySerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True}, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
