from rest_framework import serializers
from django.contrib.auth import get_user_model

from rest_framework_jwt.settings import api_settings
from django.utils import timezone
import datetime

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
expires_delta = (api_settings.JWT_REFRESH_EXPIRATION_DELTA) - datetime.timedelta(seconds=200)

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})
    token = serializers.SerializerMethodField(read_only=True)
    expires = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password2',
            'token',
            'expires',
        ]
    
    def validate_username(self,value):
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("Same username already exists!")
        return value

    def validate(self, data):
        ps = data.get('password')
        ps2 = data.get('password2')
        if ps!=ps2:
            raise serializers.ValidationError("Passwords must match!")
        return data

    def create(self, validated_data):
        user_obj = User(username=validated_data.get('username'))
        user_obj.set_password(validated_data.get('password'))
        user_obj.save()
        return user_obj

    def get_token(self, obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def get_expires(self, obj):
        return (timezone.now() + expires_delta)