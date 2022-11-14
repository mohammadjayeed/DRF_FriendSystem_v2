from django.db import transaction
from rest_framework import generics
from rest_framework import status as s
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import permission_classes

from social_app.models import *

from .serializers import *


class ProfileViewSet(ListModelMixin, GenericViewSet):
    
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(user_id=self.request.user.id)

    def get_serializer_context(self):
        return {'user_id':self.request.user.id}




class AllProfileList(generics.ListAPIView):             
    queryset = Profile.objects.all()
    serializer_class = AllProfileListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user__user_name']
    permission_classes = [IsAuthenticatedOrReadOnly]



@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def send_invite(request,pk):
    with transaction.atomic():
        sender = Profile.objects.get(id=request.user.id)
        receiver = Profile.objects.get(id=pk)


        friend_object, created = Friendship.objects.get_or_create(sender=sender,receiver=receiver,status='send')

        if not created:
            return Response({'error': 'you already sent him a request'}, status=s.HTTP_400_BAD_REQUEST)
        
        friend_object.save()
            
            
    return Response(status=s.HTTP_201_CREATED)





@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def decline_invite(request,pk):
    with transaction.atomic():
        try:
            receiver = Profile.objects.get(id=request.user.id)
            sender = Profile.objects.get(id=pk)
            friend_object = Friendship.objects.get(sender=sender,receiver=receiver)
            sender.friends.remove(receiver.user)
            receiver.friends.remove(sender.user)
            friend_object.delete()
        except Friendship.DoesNotExist:
            return Response(status=s.HTTP_204_NO_CONTENT)

        
    return Response(status=s.HTTP_200_OK)

