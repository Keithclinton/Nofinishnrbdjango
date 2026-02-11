from django.urls import path
from .views import RegisterView, LoginView, MeView
from .registration_views import IndividualRegistrationView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('me/', MeView.as_view(), name='me'),
    path('registrations/individual/', IndividualRegistrationView.as_view(), name='individual-registration'),
]
