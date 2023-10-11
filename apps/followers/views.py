from django.conf import settings
from rest_framework import generics, permissions, views, response, status

from ..profiles.models import User
from .models import Follower
from .serializers import FollowerListSerializer


class FollowerListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowerListSerializer

    def get_queryset(self):
        return Follower.objects.filter(follower_id=self.request.user.id)


class FollowerSubscribeOrUnsubscribeView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            user = User.objects.filter(id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)

        Follower.objects.create(subscriber=request.user, user=user)
        return response.Response(status=201)

    def delete(self, request, pk):
        try:
            sub = Follower.objects.get(subscriber=request.user, user_id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        sub.delete()
        return response.Response(status=204)

    # def post(self, request, pk):
    #     try:
    #         user_to_follow = User.objects.get(pk=pk)
    #         Follower.objects.get_or_create(follower=request.user, following=user_to_follow)
    #         return response.Response({'detail': 'Subscribed'}, status=status.HTTP_201_CREATED)
    #     except User.DoesNotExist:
    #         return response.Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    #     except:
    #         return response.Response({'detail': 'Subscription failed'}, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk):
    #     try:
    #         user_to_unfollow = User.objects.get(pk=pk)
    #         Follower.objects.filter(follower=request.user, following=user_to_unfollow).delete()
    #         return response.Response({'detail': 'Unsubscribed'}, status=status.HTTP_204_NO_CONTENT)
    #     except User.DoesNotExist:
    #         return response.Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    #     except:
    #         return response.Response({'detail': 'Unsubscription failed'}, status=status.HTTP_400_BAD_REQUEST)
