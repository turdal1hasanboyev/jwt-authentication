from django.urls import path

from .views import (
    RegisterView,
    CustomLoginView,
    LogoutView,
    RefreshTokenView,
    VerifyTokenView,
    CurrentUserView,
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token-refresh/', RefreshTokenView.as_view(), name='token-refresh'),
    path('token-verify/', VerifyTokenView.as_view(), name='token-verify'),
    path('me/', CurrentUserView.as_view(), name='current-user'),
]
