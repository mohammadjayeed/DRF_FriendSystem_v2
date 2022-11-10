from django.contrib.auth.backends import ModelBackend
from .models import User

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