"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from common.blog_views import BlogPostListView, ImpactStoryListView, ClinicListView, ChallengeEntryCreateView
from common.volunteer_views import VolunteerApplicationView
from common.shop_views import ProductListView, OrderCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/donations/', include('donations.urls')),
    path('api/sponsors/', include('sponsors.urls')),
    path('api/registrations/individual/', include('users.urls')),
    path('blog', BlogPostListView.as_view(), name='blog-list'),
    path('stories', ImpactStoryListView.as_view(), name='impact-story-list'),
    path('clinics', ClinicListView.as_view(), name='clinic-list'),
    path('challenge', ChallengeEntryCreateView.as_view(), name='challenge-entry-create'),
    path('volunteers/', VolunteerApplicationView.as_view(), name='volunteer-application'),
    path('shop/products/', ProductListView.as_view(), name='shop-products'),
    path('shop/orders/', OrderCreateView.as_view(), name='shop-orders'),
]
