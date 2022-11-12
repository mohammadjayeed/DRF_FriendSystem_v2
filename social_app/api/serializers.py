from rest_framework import serializers
from social_app.models import *

class ProfileSerializer(serializers.ModelSerializer):
    friends_ = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = ['friends_']

    def get_friends_(self, profile : Profile):
        return profile.friends.values('id','user_name')