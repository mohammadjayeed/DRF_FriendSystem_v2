from rest_framework import serializers
from social_interaction_app.models import *
from social_app import *
from django.conf import settings
from itertools import chain

class FriendsPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['myposts','id','post_box','likes'] #,'likes'

    likes = serializers.SerializerMethodField()
    myposts = serializers.SerializerMethodField()

    def get_likes(self, post: Post):
        profile = self.context['profile']
        # like = self.context['like']
        if profile in post.liked.all():
            return True

        return False

    def get_myposts(self, post:Post):
        post = self.context['post_']
        # like = self.context['like']
        posts = post.all().values_list('post_box')
        
        return posts

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id','post_box']

    def create(self, validated_data):
        user_id = self.context['user_id']
        new_object = Post.objects.create(owner_id=user_id, **validated_data)
        return new_object

