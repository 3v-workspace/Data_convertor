from django.shortcuts import render

from rest_framework import generics

from . import models
from . import serializers

class UserListView(generics.ListAPIView):
    queryset = models.DataOceanUser.objects.all()
    serializer_class = serializers.UserSerializer