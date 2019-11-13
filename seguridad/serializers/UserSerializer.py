from django.contrib.auth import password_validation as validators
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from seguridad.models import Profile
from seguridad.serializers import UserProfileSerializer


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    username = serializers.CharField(validators=[
        UniqueValidator(queryset=User.objects.all(), message="Existe un usuario con la misma denominación.")])
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all(), message="Existe un usuario con el mismo correo.")])

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        if self.context['request'].method == 'PUT':
            self.fields.pop('password')

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'is_active',
            'profile',
            'groups',
            'user_permissions'
        )

    # def validate(self, data):
    #
    #     profile_data = data.pop('profile')
    #     groups = data.pop('groups') if 'groups' in data else None
    #     permissions = data.pop('user_permissions') if 'user_permissions' in data else None
    #
    #     if 'password' in self.fields:
    #         user = User(**data)
    #         password = data.get('password')
    #
    #         errors = dict()
    #         try:
    #             validators.validate_password(password=password, user=user)
    #         except ValidationError as e:
    #             errors['password'] = list(e.messages)
    #
    #         if errors:
    #             raise serializers.ValidationError(errors)
    #
    #     data['profile'] = profile_data
    #     if groups:
    #         data['groups'] = groups
    #     if permissions:
    #         data['user_permissions'] = permissions
    #     return super(UserSerializer, self).validate(data)
    #
    # def create(self, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     password = validated_data.pop('password')
    #
    #     user = super(UserSerializer, self).create(validated_data)
    #     user.set_password(password)
    #     # user.save()
    #     profile = Profile.objects.get(user_id=user.id)
    #     if profile is None:
    #         profile = Profile(user=user, **profile_data)
    #     else:
    #         for attr, value in profile_data.items():
    #             setattr(profile, attr, value)
    #     profile.save()
    #
    #     return user
    #
    # def update(self, instance, validated_data):
    #
    #     profile_data = validated_data.pop('profile')
    #
    #     instance = super(UserSerializer, self).update(instance, validated_data)
    #
    #     profile = instance.profile if hasattr(instance, 'profile') else Profile()
    #     profile.theme = profile_data.get('theme', profile.theme)
    #     profile.language = profile_data.get('language', profile.language)
    #     profile.photo = profile_data.get('photo', profile.photo)
    #     if not hasattr(instance, 'profile'):
    #         profile.user = instance
    #     profile.save()
    #
    #     return instance
