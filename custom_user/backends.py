from django.contrib.auth.backends import ModelBackend
from .models import User
from django.core.management.utils import get_random_secret_key



class UserBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['email']
        otp = kwargs['otp']
        
        try:
            user_obj = User.objects.get(email=email)
            if user_obj.otp == otp:
                return user_obj
        except User.DoesNotExist:
            pass
