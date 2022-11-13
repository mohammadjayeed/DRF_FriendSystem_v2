from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from social_interaction_app.models import *
from .serializers import *
from itertools import chain
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import FriendsPostSerializer

class FriendsPostViewSet(CreateModelMixin,ListModelMixin, GenericViewSet):

    serializer_class = FriendsPostSerializer


    # def get_serializer_class(self):
    #     if self.request.method == "POST":
    #         return PostSerializer
    #     elif self.request.method == "GET":
    #         return FriendsPostSerializer
        

        

    def get_queryset(self):

        queryset = Profile.objects.prefetch_related('posts').prefetch_related('like_link').get(user = self.request.user)
        users = [user for user in queryset.friends.all()]
        posts = []
        qs = None
        for u in users:
            p = Profile.objects.get(user=u)
            p_posts = p.posts.all()
            posts.append(p_posts)
        
        if len(posts)>0:
            qs = sorted(chain(*posts), reverse=True, key=lambda obj:obj.created_at)

        return qs

    def get_serializer_context(self):
        profile = Profile.objects.get(id=self.request.user.id)
        # post = Post.objects.get(owner_id=self.request.user.id)
        # like = Like.objects.get(owner=profile, post_id=post.id)
        # print(like)
        return {'profile': profile } #,'like':like
        

class PostViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(owner_id=self.request.user.id)

    def get_serializer_context(self):
        return {'user_id':self.request.user.id}

@api_view(['POST'])
def like_unlike_post(request,pk):
    if request.method == 'POST':
        post_object = Post.objects.get(id=pk)
        profile = Profile.objects.get(id = request.user.id)

        if profile in post_object.liked.all():
            post_object.liked.remove(profile)
        else:
            post_object.liked.add(profile)

        like,created = Like.objects.get_or_create(owner=profile, post_id=pk)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
            
            post_object.save()
            like.save()

        return Response(status=status.HTTP_200_OK)
            


