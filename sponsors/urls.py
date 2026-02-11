from django.urls import path
from .views import SponsorCreateView, SponsorListView, SponsorStatusUpdateView

urlpatterns = [
    path('', SponsorListView.as_view(), name='sponsor-list'),
    path('create/', SponsorCreateView.as_view(), name='sponsor-create'),
    path('<int:pk>/status/', SponsorStatusUpdateView.as_view(), name='sponsor-status-update'),
]
