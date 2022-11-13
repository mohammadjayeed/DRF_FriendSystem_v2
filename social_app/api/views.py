from social_app.models import *
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import *
from rest_framework.decorators import api_view
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status as s
from rest_framework.filters import SearchFilter
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

class ProfileViewSet(ListModelMixin, GenericViewSet):
    
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.prefetch_related('posts').filter(user_id=self.request.user.id)

    def get_serializer_context(self):
        return {'user_id':self.request.user.id}




class AllProfileList(generics.ListAPIView):             
    queryset = Profile.objects.all()
    serializer_class = AllProfileListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user__user_name']



@api_view(['POST'])
def send_invite(request,pk):
    with transaction.atomic():
        sender = Profile.objects.get(id=request.user.id)
        receiver = Profile.objects.get(id=pk)


        friend_object = Friendship()
        friend_object.sender = sender
        friend_object.receiver = receiver
        friend_object.status = 'send'
        friend_object.save()

        
    return Response(status=s.HTTP_200_OK)




@api_view(['DELETE'])
def decline_invite(request,pk):
    with transaction.atomic():
        receiver = Profile.objects.get(id=request.user.id)
        sender = Profile.objects.get(id=pk)
        friend_object = Friendship.objects.get(sender=sender,receiver=receiver )
        sender.friends.remove(receiver.user)
        receiver.friends.remove(sender.user)
        friend_object.delete()

        
    return Response(status=s.HTTP_200_OK)

