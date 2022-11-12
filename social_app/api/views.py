from django.shortcuts import render
from social_app.models import *
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import *


class ProfileViewSet(ReadOnlyModelViewSet):
    
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)