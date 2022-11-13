from rest_framework import serializers
from social_interaction_app.models import *
from social_app import *

class CommentSerializer(serializers.ModelSerializer):
    class Meta:

        model = Comment
        fields = ['id','comment_box']

    def create(self, validated_data):
        post_object = self.context['post_object']
        profile = self.context['profile']
        new_object = Comment.objects.create(owner_id=profile.id, post_id = post_object.id,**validated_data)
        return new_object


class FriendsPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id','post_box','likes','comments']

    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    def get_likes(self, post: Post):
        return post.post_liked.values('liked')

    def get_comments(self, post: Post):
        return post.post_comment.values('comment_box')
    

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id','post_box']

    def create(self, validated_data):
        user_id = self.context['user_id']
        new_object = Post.objects.create(owner_id=user_id, **validated_data)
        return new_object

