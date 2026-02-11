from django.urls import path
from .views import DonationCreateView, DonationListView
from .public_views import PublicDonationCreateView
urlpatterns = [
    path('', DonationListView.as_view(), name='donation-list'),
    path('create/', DonationCreateView.as_view(), name='donation-create'),
    path('public/', PublicDonationCreateView.as_view(), name='public-donation-create'),
]
