from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.serializers import UserSerializer
from .registration_serializers import IndividualRegistrationSerializer

class IndividualRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        # Map frontend fields to backend fields
        full_name = data.get('fullName', '').strip()
        first_name, last_name = '', ''
        if full_name:
            parts = full_name.split()
            first_name = parts[0]
            last_name = ' '.join(parts[1:]) if len(parts) > 1 else ''
        user_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': data.get('email', ''),
            'phone': data.get('phone', ''),
            'password': data.get('password', User.objects.make_random_password()),
            'password2': data.get('password', User.objects.make_random_password()),
            'role': 'user',
        }
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            user = User.objects.create_user(
                email=user_data['email'],
                password=user_data['password'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                phone=user_data['phone'],
                role='user',
            )
            reg_data = {
                'user': user.id,
                'group_type': data.get('groupType', ''),
                'emergency_contact_name': data.get('emergencyContact', {}).get('name', ''),
                'emergency_contact_phone': data.get('emergencyContact', {}).get('phone', ''),
                'date_of_birth': data.get('dateOfBirth', None),
                'race_category': data.get('raceCategory', ''),
            }
            reg_serializer = IndividualRegistrationSerializer(data=reg_data)
            if reg_serializer.is_valid():
                reg_serializer.save(user=user)
                return Response({'success': True, 'user_id': user.id, 'email': user.email}, status=status.HTTP_201_CREATED)
            else:
                user.delete()
                return Response({'success': False, 'errors': reg_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
