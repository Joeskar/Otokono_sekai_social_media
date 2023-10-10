from django.shortcuts import render
from rest_framework import generics, permissions, viewsets

from .models import User
from .serializers import GetUserSerializer


class UserOpenView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions = [permissions.AllowAny]
    serializer_class = GetUserSerializer
    