
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Sponsor
from .serializers import SponsorSerializer

class IsAdmin(permissions.BasePermission):
	def has_permission(self, request, view):
		return request.user.is_authenticated and request.user.role == 'admin'

class SponsorCreateView(generics.CreateAPIView):
	queryset = Sponsor.objects.all()
	serializer_class = SponsorSerializer
	permission_classes = [permissions.IsAuthenticated]

class SponsorListView(generics.ListAPIView):
	queryset = Sponsor.objects.all()
	serializer_class = SponsorSerializer
	permission_classes = [IsAdmin]

class SponsorStatusUpdateView(generics.UpdateAPIView):
	queryset = Sponsor.objects.all()
	serializer_class = SponsorSerializer
	permission_classes = [IsAdmin]
	http_method_names = ['put']
