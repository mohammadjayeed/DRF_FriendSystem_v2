from custom_user.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from custom_user.models import User as user
from django.contrib.auth import authenticate
from rest_framework_simplejwt.settings import api_settings
from rest_framework import exceptions
from rest_framework_simplejwt.serializers import PasswordField
from django.conf import settings
from custom_user.backends import UserBackend
from django.contrib.auth.models import update_last_login
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.CharField()
        del self.fields["password"]
        self.fields["otp"] = serializers.CharField()
        

        

    def validate(self, attrs):
        
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            "otp": attrs["otp"]
        }
        
        try:
            authenticate_kwargs["request"] = self.context["request"]
        except KeyError:
            pass

        self.user = UserBackend.authenticate(self,**authenticate_kwargs)

        if not api_settings.USER_AUTHENTICATION_RULE(self.user):
            raise exceptions.AuthenticationFailed(
                self.error_messages["no_active_account"],
                "no_active_account",
            )
        
        data = {}
        
        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
    # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)
    #     return token

        


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields =  ['email','user_name', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'error': 'passwords did not match'})

        user = User(email=self.validated_data['email'],
                    user_name=self.validated_data['user_name'],is_active=True)
        user.set_password(self.validated_data['password'])
        user.save()
        return user