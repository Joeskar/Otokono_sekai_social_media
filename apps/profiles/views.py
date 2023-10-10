from rest_framework import generics, permissions, viewsets
from rest_framework.generics import get_object_or_404

from .models import User
from .serializers import GetUserSerializer, GetPublicUserSerializer


class UserPublicView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = GetPublicUserSerializer


class UserPrivateView(generics.RetrieveUpdateAPIView):
    serializer_class = GetUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_object(self):
        obj = get_object_or_404(self.get_queryset())
        self.check_object_permissions(self.request, obj)
        return obj
