from rest_framework import serializers, status
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from seguridad.models import Profile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('company', 'name', 'last_name', 'country', 'city', 'zipcode', 'avatar')


class UserProfileAvatarSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(allow_null=True,required=False)

    class Meta:
        model = Profile
        fields = ('name', 'last_name', 'country', 'city', 'zipcode', 'avatar')
