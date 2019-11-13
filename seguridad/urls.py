from django.conf.urls import url
# from seguridad import XipacExpiringToken
from django.urls import path
from djoser import views as djoser_views
# from seguridad.views import CustomPasswordResetView
from seguridad.views import UserViewSet, ProfileView

urlpatterns = [
    # url(r'^api-token-auth/', XipacExpiringToken.obtain_expiring_auth_token),
    # url(r'^password/reset/confirm', djoser_views.PasswordResetConfirmView.as_view()),
    # url(r'^password/reset', CustomPasswordResetView.as_view()),
    path('user/<pk>/changeprofile/', ProfileView.as_view())
]
