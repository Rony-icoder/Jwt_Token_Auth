from django.contrib import admin
from django.urls import path, include
from .views import RegisterView, CreateTokenView

from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView, TokenVerifyView )

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("token/", CreateTokenView.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

