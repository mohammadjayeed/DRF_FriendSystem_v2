from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from social_interaction_app.models import *
from .serializers import *
from itertools import chain
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .serializers import FriendsPostSerializer
from rest_framework.permissions import IsAuthenticated
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.generics import ListAPIView

class CommentViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        post_object = Post.objects.get(id=self.kwargs['posts_pk'])
        profile = Profile.objects.get(id =self.request.user.id)
        return {'post_object':post_object , 'profile':profile}


class PostViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Post.objects.filter(owner_id=self.request.user.id)

    def get_serializer_context(self):
        return {'user_id':self.request.user.id}

class FriendsPostViewSet(CreateModelMixin,ListModelMixin, GenericViewSet):

    serializer_class = FriendsPostSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):

        queryset = Profile.objects.prefetch_related('posts'). \
            prefetch_related('like_link'). \
            prefetch_related('comment_link'). \
            get(user = self.request.user)

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
        return {'profile': profile } 
        

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def like_unlike_post(request,pk):
    if request.method == 'POST':
        post_object = Post.objects.get(id=pk)
        profile = Profile.objects.get(id = request.user.id)

        if profile in post_object.pliked.all():
            post_object.pliked.remove(profile)
        else:
            post_object.pliked.add(profile)

        like,created = Like.objects.get_or_create(owner=profile, post_id=pk)

        if not created:
            if like.liked == 'True':
                like.liked = 'False'
            else:
                like.liked = 'True'
            
            post_object.save()
            like.save()

        return Response(status=status.HTTP_200_OK)
            


