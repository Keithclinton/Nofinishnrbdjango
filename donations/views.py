
from rest_framework import generics, permissions
from .models import Donation
from .serializers import DonationSerializer

class DonationCreateView(generics.CreateAPIView):
	queryset = Donation.objects.all()
	serializer_class = DonationSerializer
	permission_classes = [permissions.IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class DonationListView(generics.ListAPIView):
	serializer_class = DonationSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		return Donation.objects.filter(user=self.request.user)
