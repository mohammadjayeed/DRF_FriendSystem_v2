from rest_framework import serializers
from social_interaction_app.models import *
from social_app import *
from django.conf import settings
class FriendsPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id','post_box']



class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id','post_box']

    def create(self, validated_data):
        user_id = self.context['user_id']
        new_object = Post.objects.create(owner_id=user_id, **validated_data)
        return new_object

