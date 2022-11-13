from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from social_interaction_app.models import *
from .serializers import *
from itertools import chain
from rest_framework import views
from rest_framework.response import Response

from .serializers import FriendsPostSerializer

class FriendsPostViewSet(ListModelMixin, GenericViewSet):

    serializer_class = FriendsPostSerializer

    def get_queryset(self):

        queryset = Profile.objects.get(user = self.request.user)
        users = [user for user in queryset.friends.all()]
        posts = []
        qs = None
        for u in users:
            p = Profile.objects.get(user=u)
            p_posts = p.posts.all()
            posts.append(p_posts)
        
        if len(posts)>0:
            qs = sorted(chain(*posts), reverse=True, key=lambda obj:obj.created_at)

        print(qs)
        print(type(qs))
        return qs
        
        
       


class PostViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(owner_id=self.request.user.id)

    def get_serializer_context(self):
        return {'user_id':self.request.user.id}