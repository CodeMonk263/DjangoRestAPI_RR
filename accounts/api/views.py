from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework_jwt.settings import api_settings
from django.utils import timezone
from .serializers import UserRegistrationSerializer
import datetime

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
expires_delta = (api_settings.JWT_REFRESH_EXPIRATION_DELTA) - datetime.timedelta(seconds=200)

User = get_user_model()

class AuthenticationAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return Response({"response": "You are authenticated!"})
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)

        qs = User.objects.filter(
            Q(username__iexact=username),
        ).distinct()
        if qs.count()==1:
            user_obj = qs.first()
            if (user_obj.check_password(password)):
                user = user_obj
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                return Response({'token': token,
                                'user': user.username,
                                'expires': timezone.now() + expires_delta})
        return Response({"error": "Invalid Creds! Please try again :("}, status=401)

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]