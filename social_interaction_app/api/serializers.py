from rest_framework import serializers
from social_interaction_app.models import *
from social_app import *
from django.conf import settings
from itertools import chain

class FriendsPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id','post_box','likes'] #,'likes' 'myposts',

    likes = serializers.SerializerMethodField()
    # myposts = serializers.SerializerMethodField()

    def get_likes(self, post: Post):
        print(post.post_liked.values('value'))
        return post.post_liked.values('value')
    

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id','post_box']

    def create(self, validated_data):
        user_id = self.context['user_id']
        new_object = Post.objects.create(owner_id=user_id, **validated_data)
        return new_object

