from django.shortcuts import render, redirect
from django.contrib.auth.models import Permission, ContentType, User, Group
# Create your views here.
from rest_framework import status
from rest_framework.decorators import action, api_view
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from seguridad.serializers import UserSerializer
from seguridad.serializers.UserProfileSerializer import UserProfileAvatarSerializer
from main_app import MainAppViewSet
from main_app.settings import SPA_URL


class UserActivationView(APIView):
    def get(self, request, uid, token):
        post_data = {'uid': uid, 'token': token}
        url = '{}/{}/{}/{}'.format(SPA_URL, 'activate', uid, token)
        return redirect(url)

    permission_classes = [AllowAny]


class UserViewSet(MainAppViewSet.MainAppViewSetMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('username', 'first_name', 'last_name', 'email')

    @action(methods=['get'], detail=True, permission_classes=[IsAuthenticated], url_name="profile")
    def profile(self, request, pk=None):
        usuario = request.user
        serializer = UserSerializer(usuario, context={'request': request})
        return Response(serializer.data)


class ProfileView(APIView):
    permission_classes = [AllowAny]

    def put(self, request,pk=None, *args, **kwargs):
        file_serializer = UserProfileAvatarSerializer(data=request.data)

        if file_serializer.is_valid():
            user = request.user
            profile = user.profile
            validated = file_serializer.validated_data
            if validated.get('name'):
                profile.name = validated.get('name')
            if validated.get('last_name'):
                profile.last_name = validated.get('last_name')
            if validated.get('zipcode'):
                profile.zipcode = validated.get('zipcode')
            if validated.get('city'):
                profile.city = validated.get('city')
            if validated.get('country'):
                profile.country = validated.get('country')
            if validated.get('avatar'):
                profile.avatar = request.data['avatar']

            profile.save(update_fields=['name', 'last_name', 'country', 'city', 'zipcode', 'avatar'])
            return Response({"message":"Su perfil se ha actualizado!!",
                             "data":  {
                                 "name":profile.name,
                                 "last_name": profile.last_name,
                                 "zipcode": profile.zipcode,
                                 "city": profile.city,
                                 "country": profile.country,
                                 "avatar": profile.avatar.url,
                             }}, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
