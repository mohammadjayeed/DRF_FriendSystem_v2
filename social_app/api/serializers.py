from rest_framework import serializers
from social_app.models import *
from social_interaction_app.models import *

class ProfileSerializer(serializers.ModelSerializer):
    my_friends = serializers.SerializerMethodField()
    
    class Meta:
        model = Profile
        fields = ['my_friends']  
    
    def get_my_friends(self,profile: Profile):

        data = {}
        data["friend_name"] = profile.friends.values('id','user_name')
        return data

class AllProfileListSerializer(serializers.ModelSerializer):
    profiles = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['profiles']

    def get_profiles(self, profile : Profile):
        data = {}
        data['username'] = profile.user.user_name
        data['id'] = profile.user.id
        return data



    