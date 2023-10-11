from rest_framework import serializers
from .models import Follower


class FollowerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ('id', 'follower', 'following')
