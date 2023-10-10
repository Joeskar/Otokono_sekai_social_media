from rest_framework import serializers

from .models import User


class GetPublicUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = (
            "id",
            "first_login",
            "password",
            "email",
            "avatar",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
            "date_joined"
        )


class GetUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = (
            "email",
            "phone_number",
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )
